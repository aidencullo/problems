class Solution:

    def longestPalindrome(self, s: str) -> str:
        pal = ""
        for x in range(len(s)):
            current = self.check_pals(s[x:])
            pal = current if len(current) > len(pal) else pal
        return pal

    def check_pals(self, s):
        bld = ""
        for c in s:
            bld += c
            if self.is_palindrome(bld):
                pal = bld
        return pal

    def is_palindrome(self, s):
        for x in range(len(s)//2):
            if s[x] != s[len(s)-1-x]:
                return False
        return True
