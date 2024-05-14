class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        n = len(nums[0])
        for i in range(2 ** n):
            binary = bin(i)[2:].zfill(n)
            if not binary in nums:
                return binary
        return ""
