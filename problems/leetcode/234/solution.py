from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cnt = self.count(head)
        mid = cnt // 2
        even = cnt % 2 == 0
        stack = []
        for i in range(cnt):
            if i < mid:
                stack.append(head.val)
            if i == mid and even:
                if head.val != stack.pop():
                    return False
            if i > mid:
                if head.val != stack.pop():
                    return False
            head = head.next
        return True

    def count(self, head):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt
