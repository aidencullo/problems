from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        d = [[0] * m for _ in range(n)]
        d[0][0] = 1 if not obstacleGrid[0][0] else 0
        for i in range(n):
            for j in range(m):
                if not obstacleGrid[i][j]:
                    if i != 0:
                        d[i][j] += d[i - 1][j]
                    if j != 0:
                        d[i][j] += d[i][j - 1]
        return d[n - 1][m - 1]
