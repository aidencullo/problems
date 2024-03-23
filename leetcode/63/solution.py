# time: O(n * m)
# space: O(1)

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n):
            for j in range(m):
                if not obstacleGrid[i][j]:
                    if i == 0 and j == 0:
                        obstacleGrid[i][j] = 1
                    if i != 0:
                        obstacleGrid[i][j] += obstacleGrid[i - 1][j]
                    if j != 0:
                        obstacleGrid[i][j] += obstacleGrid[i][j - 1]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[-1][-1]
