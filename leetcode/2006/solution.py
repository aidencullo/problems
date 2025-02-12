class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        total = 0
        for x in nums:
            for y in nums:
                if x - y == k:
                    total += 1
        return total
