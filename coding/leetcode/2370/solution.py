class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if abs(ord(s[i]) - ord(s[j])) <= k:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
