class Solution:
    def perfectSum(self, arr, n, sum):
        dp = [[1] + [0] * sum for __ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(sum + 1):
                dp[i][j] = dp[i-1][j]
                if arr[i-1] <= j:
                    dp[i][j] += dp[i-1][j - arr[i-1]]
        return dp[-1][-1] % (10**9 + 7)
    


"""
[2,2,3,4,5], k = 9

    0 1 2 3 4 5 6 7 8 9
0   1 0 0 0 0 0 0 0 0 0
2   1 0 1 0 0 0 0 0 0 0
2   1 0 2 0 1 0 0 0 0 0
3   1 0 2 1 1 2 0 1 0 0
4   1 0 2 1 2 2 2 2 1 2
5   1 0 2 1 2 3 2 4 2 4
"""
