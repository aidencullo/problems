# time O(n + klogn)
# space O(n)

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums
        heapq.heapify(heap)
        for i in range(len(nums) - k + 1):
            ith = heapq.heappop(heap)
        return ith
