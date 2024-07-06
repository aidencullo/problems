class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        for i in range(n):
            for j in range(n, i, -1):
                total += len(Counter(nums[i:j])) ** 2
        return total
