class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        res = []
        n = len(nums)
        l, r = 0, n // 2
        while r < n:
            res.append(nums[l])
            res.append(nums[r])
            l += 1
            r += 1
        return res
