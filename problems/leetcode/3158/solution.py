from functools import reduce


class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        res = 0
        seen = set()
        for num in nums:
            if num in seen:
                res ^= num
            seen.add(num)
        return res
