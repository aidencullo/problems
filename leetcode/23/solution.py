import heapq
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(A, B):
            head = ListNode()
            runner = head
            while A and B:
                if A.val < B.val:
                    runner.next = A
                    A = A.next
                else:
                    runner.next = B
                    B = B.next
                runner = runner.next
            while A:
                runner.next = A
                A = A.next
                runner = runner.next
            while B:
                runner.next = B
                B = B.next
                runner = runner.next
            return head.next

        if not lists:
            return
        while len(lists) > 1:
            lists[0] = merge(lists[0], lists[-1])
            del lists[-1]
        return lists[0]
