class Solution:
    def removePalindromeSub(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return 2
            l += 1
            r -= 1
        return 1
