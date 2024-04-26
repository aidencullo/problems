class Solution:
    def isSubsetSum (self, N, arr, sum):
        # code here
        dp = [[1] + [0] * sum for __ in range(N + 1)]
        for i in range(1, N+1):
            for target in range(1, sum + 1):
                dp[i][target] = dp[i-1][target]
                if target >= arr[i-1]:
                    dp[i][target] = max(dp[i-1][target - arr[i-1]], dp[i][target])
        return dp[-1][-1]
        

assert Solution().isSubsetSum(6, [3, 34, 4, 12, 5, 2], 9) == 1
assert Solution().isSubsetSum(6, [3, 34, 4, 12, 5, 2], 30) == 0
assert Solution().isSubsetSum(6, [3, 34, 4, 12, 5, 2], 1) == 0
assert Solution().isSubsetSum(6, [3, 34, 4, 12, 5, 2], 3) == 1
assert Solution().isSubsetSum(6, [3, 34, 4, 12, 5, 2], 4) == 1
