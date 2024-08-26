class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        def count(n: int) -> int:
            cnt = 0
            while n > 0:
                cnt += n & 1
                n //= 2
            return cnt
        
        return sum(num for i, num in enumerate(nums) if count(i) == k)
