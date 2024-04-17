# O(n + nlgn) = O(nlgn) time, O(n) space

from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-val, key) for key, val in counter.items()]
        res = ''
        heapq.heapify(heap)
        while len(heap) > 1:
            val1, key1 = heapq.heappop(heap)
            val2, key2 = heapq.heappop(heap)
            res += key1
            res += key2
            val1 += 1
            val2 += 1
            if val1 != 0:
                heapq.heappush(heap, (val1, key1))
            if val2 != 0:
                heapq.heappush(heap, (val2, key2))
        if heap:
            val1, key1 = heapq.heappop(heap)
            if val1 < -1:
                return ''
            res += key1
        return res
