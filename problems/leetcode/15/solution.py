# #Solution 1
# #time limit exceeded
# from typing import Optional, List, Tuple

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         results = set()
#         for i, el1 in enumerate(nums):
#             for j, el2 in enumerate(nums):
#                 for k, el3 in enumerate(nums):
#                     if (i != j
#                         and j != k
#                         and k != i
#                         and el1 + el2 + el3 == 0):
#                         results.add(tuple(sorted([el1, el2, el3])))
#         return sorted([list(tup) for tup in results])
                







from collections import Counter
from typing import Optional, List, Tuple

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r =  i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    results.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return results
