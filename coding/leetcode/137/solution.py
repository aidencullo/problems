class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(31, -1, -1):
                bits[i] += num & 1
                num >>= 1
        bits_mod = [bit % 3 for bit in bits]
        b = ''.join(list(map(str, bits_mod)))
        return int(b, 2)
