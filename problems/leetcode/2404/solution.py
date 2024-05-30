from collections import Counter

class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        num_counter = Counter(nums)
        num_counter = {key: val for key, val in num_counter.items() if key % 2 == 0}
        if not num_counter:
            return -1
        max_val = max(num_counter.values())
        num_counter = {key: val for key, val in num_counter.items() if val == max_val}
        return min(num_counter.keys())
