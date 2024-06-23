class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def dfs(grid, row, col):
            if not (0 <= row < rows and 0 <= col < cols):
                return 1
            if (row, col) in seen:
                return 0
            if grid[row][col] == 0:
                return 1
            seen.add((row, col))
            return dfs(grid, row + 1, col) + dfs(grid, row - 1, col) + dfs(grid, row, col + 1) + dfs(grid, row, col - 1)

        seen = set()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return dfs(grid, i, j)
        return 0
