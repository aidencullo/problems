class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        res = [0] * len(nums) * 2
        l, r = 0, len(nums)
        for num in nums:
            res[l] = num
            res[r] = num
            l += 1
            r += 1
        return res
