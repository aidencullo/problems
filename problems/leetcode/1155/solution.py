# time: O(n * target * k)
# space: O(target)


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [1] + [0] * target
        MOD = 10**9 + 7

        for _ in range(min(n, target)):
            new_dp = [0] * (target + 1)
            for total in range(1, target + 1):
                for die in range(1, min(k, total) + 1):
                    new_dp[total] += dp[total - die]
            dp = new_dp

        return dp[target] % MOD
