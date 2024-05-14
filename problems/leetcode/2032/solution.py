class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        result = set()
        nums1 = set(nums1)
        nums2 = set(nums2)
        nums3 = set(nums3)
        for x in nums1:
            if x in nums2 or x in nums3:
                result.add(x)
        for x in nums2:
            if x in nums3:
                result.add(x)
        return list(result)
