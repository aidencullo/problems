class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        for i, _ in enumerate(s):
            j = k = i
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > len(longest):
                    longest = s[j:k + 1]
                j -= 1
                k += 1
            j = i
            k = i + 1
            while j >= 0 and k < len(s) and s[j] == s[k]:
                if k - j + 1 > len(longest):
                    longest = s[j:k + 1]
                j -= 1
                k += 1
        return longest
