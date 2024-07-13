class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        def dfs(i, path_len, prev):
            if i == len(nums):
                if path_len > self.LIS:
                    self.count = 1
                    self.LIS = path_len
                elif path_len == self.LIS:
                    self.count += 1
                return
            if i == 0:
                dfs(i + 1, 1, nums[i])
            if i != 0 and nums[i] > prev:
                dfs(i + 1, path_len + 1, nums[i])
            dfs(i + 1, path_len, prev)

        self.count = 0
        self.LIS = 0
        dfs(0, 0, float("-inf"))
        return self.count
