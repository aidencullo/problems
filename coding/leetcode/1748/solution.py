class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dup = set()
        seen = set()
        for num in nums:
            if num in seen:
                dup.add(num)
            seen.add(num)
        return sum(seen - dup)
