from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            while head:
                next_node = head.next
                head.next = prev
                prev = head
                head = next_node
            return prev

        head = reverse(head)
        dummy = ListNode()
        curr = dummy

        while head:
            if not curr.next:
                curr.next = head
                head = head.next
                curr.next.next = None
            elif head.val >= curr.next.val:
                curr = curr.next
                curr.next = head
                head = head.next
                curr.next.next = None
            else:
                head = head.next
        return reverse(dummy.next)
