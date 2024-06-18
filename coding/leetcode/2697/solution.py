class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s = list(s)
        n = len(s)
        for i in range(len(s) // 2):
            l = s[i]
            r = s[n - 1 - i]
            m = min(l, r, key=ord)
            s[i] = m
            s[n - 1 - i] = m
        return ''.join(s)
