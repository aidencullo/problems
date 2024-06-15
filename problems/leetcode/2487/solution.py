from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                next = node.next
                node.next = prev
                prev = node
                node = next
            return prev


        head = reverse(head)
        runner = head
        while runner.next:
            if runner.next.val < runner.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        return reverse(head)
















































# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         def reverse(head):
#             prev = None
#             while head:
#                 next_node = head.next
#                 head.next = prev
#                 prev = head
#                 head = next_node
#             return prev

#         head = reverse(head)
#         dummy = ListNode()
#         curr = dummy

#         while head:
#             if not curr.next or head.val > curr.next.val:
#                 curr.next = head
#                 head = head.next
#                 curr = curr.next
#                 curr.next = None
#             else:
#                 head = head.next

#         return reverse(dummy.next)
