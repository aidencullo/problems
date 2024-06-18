from typing import Optional


class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a = self.count(headA)
        b = self.count(headB)
        if a > b:
            for _ in range(a - b):
                headA = headA.next
        else:
            for _ in range(b - a):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def count(self, head: ListNode):
        cnt = 0
        while head:
            head = head.next
            cnt += 1
        return cnt
