class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        def op(nums: list[int]) -> list[int]:
            for i in range(len(nums) - 1):
                if nums[i] == nums[i + 1]:
                    nums[i] *= 2
                    nums[i + 1] = 0
            return nums

        def moveZeroes(nums: list[int]) -> list[int]:
            l, r = 0, 0
            n = len(nums)
            while r < n:
                while nums[r] == 0 and r < n - 1:
                    r += 1
                nums[l], nums[r] = nums[r], nums[l]
                r += 1
                l += 1
            return nums

        return moveZeroes(op(nums))
