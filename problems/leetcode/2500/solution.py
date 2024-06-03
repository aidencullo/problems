import numpy as np


class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        res = 0
        grid = np.array(grid)
        for i, row in enumerate(grid):
            grid[i].sort()
        for j, __ in enumerate(grid[0]):
            res += max(grid[:, j])
        return res
