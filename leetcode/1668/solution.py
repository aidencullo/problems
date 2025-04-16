class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        def beginsWord(i):
            if i + m > n:
                return False
            for j in range(m):
                if sequence[i + j] != word[j]:
                    return False
            return True

        n = len(sequence)
        m = len(word)
        startsWord = [0] * n
        dp = list(startsWord)
        for i, letter in enumerate(sequence):
            if beginsWord(i):
                startsWord[i] = 1
        for i, letter in enumerate(sequence):
            dp[i] = startsWord[i]
            if i >= m and dp[i]:
                dp[i] += dp[i - m]
        return max(dp)
