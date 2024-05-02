from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        i = 1
        runner = head
        while i < right:
            runner = runner.next
            i += 1
        after_reverse = runner.next
        runner.next = None

        before_head = ListNode(0, head)
        runner = before_head
        for __ in range(1, left):
            runner = runner.next

        before_reverse = runner
        runner = runner.next

        last = after_reverse
        for __ in range(left, right + 1):
            tmp = runner.next
            runner.next = last
            last = runner
            runner = tmp

        before_reverse.next = last
        return before_head.next
    
    def print(self, head):
        while head:
            print(head.val)
            head = head.next
