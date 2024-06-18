class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalidrome(t):
            return t == t[::-1]
        
        if isPalidrome(s):
            return 1
        return 2
