import heapq
import math


class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for i in range(k):
            heapq.heappush(gifts, -math.floor(math.sqrt(-heapq.heappop(gifts))))
        return -sum(gifts)
