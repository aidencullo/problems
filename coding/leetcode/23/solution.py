import heapq
from typing import Optional

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            runner = l
            while runner:
                heapq.heappush(heap, runner.val)
                runner = runner.next
        head = ListNode(0)
        runner = head
        while heap:
            runner.next = ListNode(heapq.heappop(heap))
            runner = runner.next
        return head.next
