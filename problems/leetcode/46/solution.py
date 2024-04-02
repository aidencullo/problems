# Solution for LeetCode problem "46. Permutations"
# https://leetcode.com/problems/permutations/
# O(n!) time and space

"""
Given a collection of distinct integers, return all possible permutations.

Example:

    Input: [1,2,3]

    Output:
    [
        [1,2,3],
        [1,3,2],
        [2,1,3],
        [2,3,1],
        [3,1,2],
        [3,2,1]
    ]
"""

"""
Solution 1

Runtime
29
ms
Beats
98.52%
of users with Python3 submissions
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        mem = {}
        def subPermute(nums):
            if not nums:
                return [[]]
            res = []
            for i, num in enumerate(nums):
                dp_key = tuple(nums[:i] + nums[i + 1:])
                if dp_key in mem:
                    subPermutations = mem[dp_key]
                else:
                    subPermutations = subPermute(nums[:i] + nums[i + 1:])
                    mem[dp_key] = subPermutations
                for subPermutation in subPermutations:
                    res.append([num] + subPermutation)
            return res
        return subPermute(nums)
