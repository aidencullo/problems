from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack = []
        max_pair_sum = 0
        n = 0
        runner = head
        while runner:
            n += 1
            runner = runner.next
        n //= 2
        runner = head
        while runner:
            if n > 0:
                stack.append(runner.val)
            else:
                max_pair_sum = max(max_pair_sum, runner.val + stack.pop())
            runner = runner.next
            n -= 1
        return max_pair_sum
