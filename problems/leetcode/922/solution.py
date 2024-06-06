class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        n = len(nums)
        even, odd = 0, 0
        i = 0
        while i < n:
            while even < n and nums[even] % 2 == 1:
                even += 1
            while odd < n and nums[odd] % 2 == 0:
                odd += 1
            if i % 2 == 0:
                nums[i], nums[even] = nums[even], nums[i]
                i, even = i, even
                even += 1
            else:
                nums[i], nums[odd] = nums[odd], nums[i]
                i, odd = i, odd
                odd += 1
            i += 1
        return nums
