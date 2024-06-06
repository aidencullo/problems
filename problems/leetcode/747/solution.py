class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        idx = nums.index(max(nums))
        nums.sort()
        if 2 * nums[-2] <= nums[-1]:
            return idx
        return -1

