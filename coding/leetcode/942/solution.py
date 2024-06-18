class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        nums = list(range(n + 1))
        res = [0] * (n + 1)
        for i, char in enumerate(s):
            if char == 'D':
                res[i] = nums.pop()
            if char == 'I':
                res[i] = nums.pop(0)
        res[-1] = nums.pop()
        return res
