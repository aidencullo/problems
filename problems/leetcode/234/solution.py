from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        self.current = None
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.current = head
        return self.solve(head)

    def solve(self, head):
        if not head:
            return True
        if not self.solve(head.next):
            return False
        if head.val != self.current.val:
            return False
        self.current = self.current.next
        return True
