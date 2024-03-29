from typing import List
import numpy as np

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums)) + [float('inf')]
        nums_to_index = {num: i for i, num in enumerate(sorted_nums)}
        index_to_sort_index = [nums_to_index[num] for num in nums]
        n = len(nums)
        m = len(sorted_nums)
        d = [[0 for i in range(m)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m):
                if j:
                    if nums[i - 1] < sorted_nums[j]:
                        d[i][j] = max(d[i - 1][j], d[i - 1][index_to_sort_index[i - 1]] + 1)
                    else:
                        d[i][j] = d[i - 1][j]
        return d[-1][-1]
