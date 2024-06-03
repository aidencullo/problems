class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        result = 0
        while grid[0]:
            result += max(max(row) for row in grid)
            for i, row in enumerate(grid):
                grid[i].remove(max(row))
        return result
