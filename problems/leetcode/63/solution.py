from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def get_paths(row, col):
            if row == len(obstacleGrid):
                return 0
            if col == len(obstacleGrid[0]):
                return 0
            if obstacleGrid[row][col]:
                return 0
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                return 1
            return get_paths(row + 1, col) + get_paths(row, col + 1)
        return get_paths(0, 0)
