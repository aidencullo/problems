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
        runner = head
        reverse_runner = ListNode(0)
        while runner:
            reverse_node = ListNode(runner.val)
            reverse_node.next = reverse_runner.next
            reverse_runner.next = reverse_node
            runner = runner.next
        return reverse_runner.next
