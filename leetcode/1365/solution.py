class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        t = nums[:]
        d = {}
        t.sort()
        for i, el in enumerate(t):
            if t[i] in d:
                continue
            d[t[i]] = i
        return [d[num] for num in nums]
