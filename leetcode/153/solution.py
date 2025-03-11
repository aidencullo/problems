# from typing import List


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         l, r = 0, len(nums) - 1

#         while l < r:
#             k = (l + r) // 2
#             mid = nums[k]
#             upper = nums[r]

#             if mid < upper:
#                 r = k
#             else:
#                 l = k + 1

#         return nums[l]









class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l = 0
        r = len(nums) - 1
        while 1:
            m = (l + r) // 2
            if nums[l] < nums[m] and nums[m] < nums[r]:
                return nums[l]
            if nums[l] < nums[m]:
                l = m
                continue
            if nums[m] < nums[r]:
                r = m
                continue
            return nums[r]
            