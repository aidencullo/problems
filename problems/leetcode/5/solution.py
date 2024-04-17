# time O(n^2)
# space O(1)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check_palindrome_odd(start) -> None:
            l = r = start
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            length = (r-1) - (l+1) + 1
            if length > self.longest_len:
                self.longest_len = length
                self.longest_idx = l + 1

        def check_palindrome_even(start) -> None:
            l = start
            r = start + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            length = (r-1) - (l+1) + 1
            if length > self.longest_len:
                self.longest_len = length
                self.longest_idx = l + 1

        self.longest_len = 0
        self.longest_idx = -1
        for i, letter in enumerate(s):
            check_palindrome_even(i)
            check_palindrome_odd(i)
        return s[self.longest_idx: self.longest_idx + self.longest_len]
