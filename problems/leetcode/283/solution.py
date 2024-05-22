class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, 0
        n = len(nums)
        while r < n:
            while nums[r] == 0 and r < n - 1:
                r += 1
            nums[l], nums[r] = nums[r], nums[l]
            r += 1
            l += 1
