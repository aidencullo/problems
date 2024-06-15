from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        while head:
            while stack and stack[-1] < head.val:
                stack.pop()
            stack.append(head.val)
            head = head.next
        new_head = ListNode()
        runner = new_head
        for el in stack:
            runner.next = ListNode(el)
            runner = runner.next
        return new_head.next
