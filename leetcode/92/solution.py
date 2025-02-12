from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before_head = ListNode(0, head)
        after_reverse = self.get_nth_node(before_head, right + 2)
        before_reverse = self.get_nth_node(before_head, left)
        runner = before_reverse.next

        last = after_reverse
        for __ in range(left, right + 1):
            tmp = runner.next
            runner.next = last
            last = runner
            runner = tmp

        before_reverse.next = last
        return before_head.next

    def get_nth_node(self, head, n):
        runner = head
        for __ in range(1, n):
            runner = runner.next
        return runner

    def print(self, head):
        while head:
            print(head.val)
            head = head.next
