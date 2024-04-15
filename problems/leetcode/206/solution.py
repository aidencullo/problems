# time O(n)
# space O(n)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        new_head = ListNode(0)
        runner = new_head
        while stack:
            runner.next = ListNode(stack.pop())
            runner = runner.next
        return new_head.next
