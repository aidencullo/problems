from typing import Optional, List, Tuple
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        visited = []
        to_rot = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.append((i, j))
                    to_rot = -1
        while q:
            to_rot +=1
            qlen = len(q)
            for _ in range(qlen):
                i, j = q.popleft()
                grid[i][j] = 0
                if 0 <= i + 1 < m and 0 <= j < n and (i + 1, j) not in visited and grid[i + 1][j]:
                    q.append((i + 1, j))
                    visited.append((i + 1, j))
                if 0 <= i - 1 < m and 0 <= j < n and (i - 1, j) not in visited and grid[i - 1][j]:
                    q.append((i - 1, j))
                    visited.append((i - 1, j))
                if 0 <= i < m and 0 <= j + 1 < n and (i, j + 1) not in visited and grid[i][j + 1]:
                    q.append((i, j + 1))
                    visited.append((i, j + 1))
                if 0 <= i < m and 0 <= j - 1 < n and (i, j - 1) not in visited and grid[i][j - 1]:
                    q.append((i, j - 1))
                    visited.append((i, j - 1))
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return to_rot
