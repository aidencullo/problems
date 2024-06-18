class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            n = len(word)
            if any(word[i] != word[n - 1 - i] for i in range(n // 2)):
                continue
            return word
        return ""
