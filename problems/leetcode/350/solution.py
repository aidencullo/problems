from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()

        n = len(nums1)
        m = len(nums2)
        result = []
        l = 0
        r = 0
        while l < n and r < m:
            if nums1[l] == nums2[r]:
                result.append(nums1[l])
                l += 1
                r += 1
            elif nums1[l] < nums2[r]:
                l += 1
            else:
                r += 1
        return result
