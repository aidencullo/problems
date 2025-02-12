class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        total = sum(nums)
        max_sub = total
        while l <= r:
            if nums[l] < nums[r]:
                total -= nums[l]
                l += 1
            else:
                total -= nums[r]
                r -= 1                
            max_sub = max(max_sub, total)
        return max_sub
