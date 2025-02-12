from collections import Counter

class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        frequencies = Counter(nums)
        return sum(val for val, freq in frequencies.items() if freq == 1)
