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
            res += key1 + key2
            if val1+1 != 0:
                heapq.heappush(heap, (val1+1, key1))
            if val2+1 != 0:
                heapq.heappush(heap, (val2+1, key2))
        if heap[0][0] < -1:
            return ''
        res += heap[0][1]
        return res
