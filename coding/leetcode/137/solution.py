class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        negatives = len([num for num in nums if num < 0])
        nums = [abs(num) for num in nums]
        bits = [0] * 32
        for num in nums:
            for i in range(31, -1, -1):
                bits[i] += num & 1
                num >>= 1
        bits_mod = [bit % 3 for bit in bits]
        total = 0
        for i in range(32):
            total <<= 1
            total |= bits_mod[i]
        if negatives % 3 == 1:
            total = -total
        return total
