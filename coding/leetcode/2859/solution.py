class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        bits = [i.bit_count() for i in range(len(nums))]
        print(bits)
        return sum(num for i, num in enumerate(nums) if bits[i] == k)
