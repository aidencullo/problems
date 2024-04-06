# time: O(n * target * k)
# space: O(target)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        MOD = 10**9 + 7

        for _ in range(n):
            new_dp = [0] * (target + 1)
            for j in range(1, target + 1):
                for l in range(1, min(k + 1, j + 1)):
                    new_dp[j] += dp[j - l]
            dp = new_dp

        return dp[-1] % MOD
