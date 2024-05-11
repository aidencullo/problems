from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        runner = head
        runner1 = list1
        runner2 = list2
        while runner1 and runner2:
            if runner1.val <= runner2.val:
                runner.next = runner1
                runner1 = runner1.next
            else:
                runner.next = runner2
                runner2 = runner2.next
            runner = runner.next
        runner.next = (runner1 or runner2)
        return head.next
