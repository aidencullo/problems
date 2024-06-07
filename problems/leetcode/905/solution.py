class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, n - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            while l < n and nums[l] % 2 == 0:
                l += 1
            while r > 0 and nums[r] % 2 == 1:
                r -= 1
        return nums
