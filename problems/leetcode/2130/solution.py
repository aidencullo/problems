from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        def reverseList(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev

        def getLength(head):
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        max_pair_sum = 0
        n = getLength(head)
        n //= 2
        runner = head
        for i in range(n):
            runner = runner.next
        new_head = reverseList(runner)
        pair_runner = new_head
        runner = head
        for i in range(n):
            max_pair_sum = max(max_pair_sum, runner.val + pair_runner.val)
            runner = runner.next
            pair_runner = pair_runner.next
        return max_pair_sum
