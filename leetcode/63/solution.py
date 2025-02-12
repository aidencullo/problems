from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        dp = [[0] * cols for __ in range(rows)]
        dp[0][0] = 1

        for col in range(cols):
            for row in range(rows):
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                if col > 0:
                    dp[row][col] += dp[row][col - 1]
                if row > 0:
                    dp[row][col] += dp[row - 1][col]
        return dp[rows - 1][cols - 1]
