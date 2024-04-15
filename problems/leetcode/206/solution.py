from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node: ListNode) -> ListNode:
            if not node.next:
                return node
            reverse_head = reverse(node.next)
            node.next.next = node
            return reverse_head
            
        if not head:
            return None
        reverse_head = reverse(head)
        head.next = None
        return reverse_head
