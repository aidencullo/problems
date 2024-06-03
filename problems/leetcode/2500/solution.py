class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        res = 0
        for i, row in enumerate(grid):
            grid[i] = sorted(row)
        print(grid)
        return res
