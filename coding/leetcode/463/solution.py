class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        def dfs(grid, row, col):
            if (row, col) in seen:
                return 0
            if grid[row][col] == 0:
                return 1

        seen = []
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return self.dfs(grid, i, j)
        return 0
            
