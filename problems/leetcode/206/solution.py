from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head.next:
                return head
            tail = reverse(head.next)
            head.next.next = head
            return tail

        if not head:
            return None
        new_head = reverse(head)
        head.next = None
        return new_head
