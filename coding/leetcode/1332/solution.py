class Solution:
    def removePalindromeSub(self, s: str) -> int:
        def isPalidrome(t):
            return all(t[i] == t[len(t) - 1 - i] for i in range(len(t) // 2))
        
        if isPalidrome(s):
            return 1
        return 2
