class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        n = len(nums)
        l, r = 0, 0
        while r < n:
            nums[l], nums[r] = nums[r], nums[l]
            while l < n and nums[l] % 2 == 0:
                l += 1
            r = l
            while r < n and nums[r] % 2 == 1:
                r += 1
        return nums
