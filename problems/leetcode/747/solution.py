class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        idx = -1
        largest = float('-inf')
        second_largest = float('-inf')
        for i, num in enumerate(nums):
            if num > largest:
                second_largest = largest
                largest = num
                idx = i
                continue
            if num > second_largest:
                second_largest = num
                continue
        if largest >= 2 * second_largest:
            return idx
        return -1
