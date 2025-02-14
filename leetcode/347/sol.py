
from typing import List
from collections import Counter


# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         freq = Counter(nums)
#         freq_sorted = sorted(freq.items(), key=lambda item: item[1], reverse=True)
#         return [key for key, value in freq_sorted[:k]]

# time O(n + nlgn + k) = O(nlgn + k) = O(nlgn)
# space O(n + n + k) = O(n)

import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = [(val, key) for key, val in freq.items()]
        heapq.heapify(heap)
        return [val for key, val in heapq.nlargest(k, heap)]