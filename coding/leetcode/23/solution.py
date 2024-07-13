import heapq
from typing import Optional

class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [l for l in lists if l]
        heap = [(l.val, i) for i, l in enumerate(lists)]
        heapq.heapify(heap)
        head = ListNode()
        runner = head
        while heap:
            _, i = heapq.heappop(heap)
            runner.next = lists[i]
            runner = runner.next
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return head.next
