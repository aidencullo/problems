import heapq


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        nums = [(-num, idx) for idx, num in enumerate(nums)]
        heapq.heapify(nums)
        val1, idx1 = heapq.heappop(nums)
        val2, idx2 = heapq.heappop(nums)
        return (-val1 - 1) * (-val2 - 1)
