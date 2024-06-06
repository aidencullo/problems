import heapq


class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        idx = nums.index(max(nums))
        heap = [-num for num in nums]
        heapq.heapify(heap)
        if -heapq.heappop(heap) >= 2 * -heapq.heappop(heap):
            return idx
        return -1
