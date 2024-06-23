class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
            else:
                dfs(i + 1)
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()
        res = []
        subset = []
        dfs(0)
        return res
