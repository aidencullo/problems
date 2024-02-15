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

        if runner1.val < runner2.val:
            sortedHead: ListNode = ListNode(runner1.val)
            runner1 = runner1.next
        else:
            sortedHead: ListNode = ListNode(runner2.val)
            runner2 = runner2.next
        sortedRunner: ListNode = sortedHead
            
        while runner1 and runner2:
            if runner1.val < runner2.val:
                sortedRunner.next = ListNode(runner1.val)
                runner1 = runner1.next
            else:
                sortedRunner.next = ListNode(runner2.val)
                runner2 = runner2.next
            sortedRunner = sortedRunner.next

        if runner1:
            remainingRunner = runner1
        else:
            remainingRunner = runner2
        while remainingRunner:
            sortedRunner.next = ListNode(remainingRunner.val)
            remainingRunner = remainingRunner.next
        return sortedHead
