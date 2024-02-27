## Solution 1
# from ll import ListNode
# from stack import Stack

# from typing import Optional, List, Tuple

# # O(n) time, O(n) space
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         s = Stack()
#         while head:
#             s.push(head.val)
#             head = head.next
#         new_head: ListNode = ListNode()
#         current = new_head
#         while s:
#             current.next = ListNode(s.pop())
#             current = current.next
#         return new_head.next



# ## Solution 2
# from typing import Optional

# from ll import ListNode

# # O(n) time, O(1) space
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = None
#         while head:
#             new_node: ListNode = ListNode(head.val)
#             new_node.next = current
#             current = new_node
#             head = head.next
#         return current




# ## Solution 3
# """
# I don't think it's any faster but turned 3 sloc to 1
# """
# from typing import Optional

# from ll import ListNode

# # O(n) time, O(n) space
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = None
#         while head:
#             current = ListNode(head.val, current)
#             head = head.next
#         return current



## Solution 4
"""
I don't believe in modifying parameters, but let's allow it here
"""
from typing import Optional

from ll import ListNode

# O(n) time, O(1) space
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        current = None
        while head:
            new_head = head.next
            head.next = current
            current = head
            head = new_head
        return current
