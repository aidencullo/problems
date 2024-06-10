from collections import Counter


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        for key, value in counter.items():
            if value > n / 4:
                return key
