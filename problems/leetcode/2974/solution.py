import heapq


class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums_sorted = [0] * 101
        result = []
        for num in nums:
            nums_sorted[num] += 1
        for i in range(1, 101):
            result.extend([i] * nums_sorted[i])
        for  i in range(0, len(result), 2):
            result[i], result[i+1] = result[i+1], result[i]
        return result

