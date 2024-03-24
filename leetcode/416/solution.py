# time complexity: O(n * d)
# space complexity: O(n * d)

# d = sum of nums / 2
# n = len(nums)

# The idea is to use dynamic programming to solve this problem.
# We can create a 2D array d where d[i][j] is True if there is a subset of the first i elements of nums that sums to j.

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        total = sum(nums)
        if total % 2 != 0:
            return False
        goal = total // 2
        return hasSubset(nums, goal)

def hasSubset(nums, target):
    n = len(nums)
    d = [[False] * (target + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        d[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if j >= nums[i - 1]:
                d[i][j] = d[i - 1][j] | d[i - 1][j - nums[i - 1]]
            else:
                d[i][j] = d[i - 1][j]
    return d[n][target]
