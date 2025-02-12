from collections import defaultdict

class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        hash_table = defaultdict(int)
        for i in range(n):
            for j in range(i, n):
                hash_table[nums[j]] += 1
                total += len(hash_table) ** 2
            hash_table.clear()
        return total
