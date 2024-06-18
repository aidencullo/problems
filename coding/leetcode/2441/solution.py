class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        max_k = -1
        for num in nums:
            if -num in nums:
                max_k = max(max_k, abs(num))
        return max_k
