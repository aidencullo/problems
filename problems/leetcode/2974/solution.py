import heapq


class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        heapq.heapify(nums)
        result = []
        while nums:
            first = heapq.heappop(nums)
            second = heapq.heappop(nums)
            result.append(second)
            result.append(first)
        return result
