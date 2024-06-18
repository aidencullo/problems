class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        hash_set = set()
        max_k = -1
        for num in nums:
            if -num in hash_set:
                max_k = max(max_k, abs(num))
            hash_set.add(num)
        return max_k
