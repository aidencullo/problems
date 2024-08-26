from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return any(freq for val, freq in Counter(nums).items() if freq > 1)
