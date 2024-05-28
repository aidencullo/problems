class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n = len(sequence)
        m = len(word)
        dp = [0] * m + [0] * n
        for index, letter in enumerate(sequence):
            if sequence[index: index + m] == word:
                dp[index] = dp[index - m] + 1
        return max(dp)
