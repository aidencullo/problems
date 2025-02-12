from collections import Counter
import heapq

class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        freqs = list(Counter(arr).values())
        half = len(arr) // 2
        neg_freqs = [-freq for freq in freqs]
        heapq.heapify(neg_freqs)
        cnt = 0
        integers = len(freqs)
        while cnt < half:
            cnt -= heapq.heappop(neg_freqs)
        
        return integers - len(neg_freqs)
