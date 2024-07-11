class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        dp = [0] * len(s2)
        for c1 in s1:
            last_dp = dp[:]
            for j, c2 in enumerate(s2):
                if j == 0:
                    if c1 == c2:
                        dp[j] = ord(c2)
                else:
                    if c1 == c2:
                        dp[j] = max(last_dp[j - 1] + ord(c2), dp[j - 1], last_dp[j])
                    else:
                        dp[j] = max(dp[j - 1], last_dp[j])
        return sum(map(ord, s2)) + sum(map(ord, s1)) - 2 * max(dp)
