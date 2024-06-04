from collections import Counter


class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        return [sum(1 for j in nums if i > j) for i in nums]
