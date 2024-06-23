import operator
from functools import reduce


class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        def dfs(i):
            nonlocal res
            if i == len(nums):
                res += reduce(operator.xor, subset, 0)
            else:
                dfs(i + 1)
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        res = 0
        subset = []
        dfs(0)
        return res
