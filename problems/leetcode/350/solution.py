from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        nums2 = Counter(nums2)
        for num in nums1:
            if nums2[num] > 0:
                result.append(num)
                nums2[num] -= 1
        return result
