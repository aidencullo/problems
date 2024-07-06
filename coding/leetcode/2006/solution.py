from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        total = 0
        for num in nums:
            total += counter[num - k]
        return total
