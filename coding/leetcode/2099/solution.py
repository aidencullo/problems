# time complexity: O(nlogn)
# space complexity: O(n)


import heapq


class Solution:
    def maxSubsequence(self, nums: list[int], k: int) -> list[int]:
        heap = []
        for i, el in enumerate(nums):
            heapq.heappush(heap, (el, i))
            if len(heap) > k:
                heapq.heappop(heap)
        return [el for el, i in sorted(heap, key=lambda x: x[1])]
