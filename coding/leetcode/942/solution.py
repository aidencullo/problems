class Solution:
    def diStringMatch(self, s: str) -> list[int]:
        n = len(s)
        if s[-1] == 'D':
            s += 'I'
        else:
            s += 'D'
        res = [0] * (n + 1)
        count = n
        for i, char in enumerate(s):
            if char == 'D':
                res[i] = count
                count -= 1
        count = 0
        for i, char in enumerate(s):
            if char == 'I':
                res[i] = count
                count += 1
        return res
