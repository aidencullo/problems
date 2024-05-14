class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r and nums[l] <= nums[l + 1] and nums[l] <= nums[r]:
            l += 1
        while l < r and nums[r] >= nums[r - 1] and nums[r] >= nums[l]:
            r -= 1
        if l == r:
            return 0
        while r < len(nums) - 1 and nums[r] == nums[r + 1]:
            r += 1
        while l > 0 and nums[l] == nums[l - 1]:
            l -= 1
        return r - l + 1
                
