class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ss = set(s)
        for i, el in enumerate(s):
            if el.swapcase() not in ss:
                l = self.longestNiceSubstring(s[:i])
                r = self.longestNiceSubstring(s[i+1:])
                return max(l, r, key=len)
        return s
