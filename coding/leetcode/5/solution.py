# time O(n^3), space O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome(l: int, r: int) -> None:
            if s[l:r+1] == s[l:r+1][::-1]:
                length = r - l + 1
                if length > self.longest_len:
                    self.longest_len = length
                    self.longest_idx = l

        self.longest_len = 0
        self.longest_idx = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                check_palindrome(i, j)
        return s[self.longest_idx: self.longest_idx + self.longest_len]
