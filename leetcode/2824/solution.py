class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j and x + y < target:
                    count += 1
        return count // 2
