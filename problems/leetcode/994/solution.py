from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        oranges = 0
        rotten = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    oranges += 1
                if grid[i][j] == 2:
                    rotten.append((i, j, 0))

        days = 0
        while rotten:
                num_rotten = len(rotten)
                for __ in range(num_rotten):
                    row, col, current_day = rotten.popleft()
                    days = max(days, current_day)
                    for dr, dc in directions:
                        new_row = row + dr
                        new_col = col + dc
                        if 0 <= new_row < n and 0 <= new_col < m and grid[new_row][new_col] == 1:
                            grid[new_row][new_col] = 2
                            rotten.append((new_row, new_col, current_day + 1))
                            oranges -= 1
        return days if oranges == 0 else -1
