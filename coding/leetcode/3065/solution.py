class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return len([num for num in nums if num < k])
