class Solution:
    def numberOfPairs(self, nums1: list[int], nums2: list[int], k: int) -> int:
        cnt = 0
        for x in nums1:
            for y in nums2:
                if x % (k * y) == 0:
                    cnt += 1
        return cnt
