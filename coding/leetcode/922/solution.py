class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        even, odd = 0, 1
        n = len(nums)
        while even < n and odd < n:
            while even < n and nums[even] % 2 == 0:
                even += 2
            while odd < n and nums[odd] % 2 == 1:
                odd += 2
            if even < n:
                nums[even], nums[odd] = nums[odd], nums[even]
        return nums
