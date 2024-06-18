class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        l1 = [x for x in nums1 if not x in nums2]
        l2 = [x for x in nums2 if not x in nums1]
        return [list(set(l1)), list(set(l2))]
