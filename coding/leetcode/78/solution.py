class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums: list[int], path: list[int]):
            if nums:
                dfs(nums[1:], path + [nums[0]])
                dfs(nums[1:], path)
            else:
                self.res.append(path)
        self.res = []
        dfs(nums, [])
        return self.res
