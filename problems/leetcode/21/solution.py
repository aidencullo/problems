from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        runner: ListNode = self
        while runner:
            values.append(runner.val)
            runner = runner.next
        return repr(values)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        runner1: ListNode = list1
        runner2: ListNode = list2

        sortedHead: ListNode = ListNode(min(runner2.val, runner1.val))
        sortedRunner: ListNode = sortedHead
        
        runner1, runner2 = stepMinRunner(runner1, runner2)
            
        while runner1 and runner2:
            sortedRunner.next = ListNode(min(runner2.val, runner1.val))
            sortedRunner = sortedRunner.next

            runner1, runner2 = stepMinRunner(runner1, runner2)

        remainingRunner = next(x for x in (runner1, runner2) if x)

        remainingRunner, sortedRunner = copyLL(remainingRunner, sortedRunner)
        return sortedHead

def stepMinRunner(r1, r2):
    if r1.val < r2.val:
        r1 = r1.next
    else:
        r2 = r2.next
    return r1, r2

def copyLL(remainingRunner, sortedRunner):
    while remainingRunner:
        sortedRunner.next = ListNode(remainingRunner.val)
        sortedRunner = sortedRunner.next
        remainingRunner = remainingRunner.next
    return remainingRunner, sortedRunner
