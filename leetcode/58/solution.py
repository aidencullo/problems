class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n - 1, -1, -1):
            if s[i] == " " and res:
                break
            if s[i] == " ":
                continue
            res += 1
        return res
