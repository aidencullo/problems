from typing import Optional, List, Tuple

from ll import ListNode
from stack import Stack

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = Stack()
        while head:
            s.push(head.val)
            head = head.next
        new_head: ListNode = ListNode()
        current = new_head
        while s:
            current.next = ListNode(s.pop())
            current = current.next
        return new_head.next

