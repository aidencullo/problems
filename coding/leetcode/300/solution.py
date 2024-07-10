class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        def backtrack(i: int, path: list[int]):
            if i == len(nums):
                nonlocal LIS
                LIS = max(LIS, len(path))
                return
            if not path or path[-1] < nums[i]:
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
            backtrack(i + 1, path)
        LIS = 0
        backtrack(0, [])
        return LIS
