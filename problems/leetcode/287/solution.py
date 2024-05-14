class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        xor_sum = 0
        for el in nums:
            if xor_sum ^ el == xor_sum:
                return el
            xor_sum ^= el
        return -1
