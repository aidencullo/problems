from collections import deque
from copy import deepcopy
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        width = len(mat[0])
        height = len(mat)
        new_mat = deepcopy(mat)

        def bfs(row, col):
            min_dist = float('inf')
            q = deque()
            q.append((row, col, 0))
            visited = [(row, col)]

            while q:
                current_row, current_col, current_dist = q.popleft()

                if current_row > height - 1 or current_row < 0 or current_col > width - 1 or current_col < 0:
                    continue

                if mat[current_row][current_col] == 0:
                    min_dist = min(min_dist, current_dist)
                    continue

                current_row += 1
                if (current_row, current_col) not in visited:
                    q.append((current_row, current_col, current_dist + 1))
                    visited.append((current_row, current_col))
                current_row -= 2
                if (current_row, current_col) not in visited:
                    q.append((current_row, current_col, current_dist + 1))
                    visited.append((current_row, current_col))
                current_row += 1
                current_col += 1
                if (current_row, current_col) not in visited:
                    q.append((current_row, current_col, current_dist + 1))
                    visited.append((current_row, current_col))
                current_col -= 2
                if (current_row, current_col) not in visited:
                    q.append((current_row, current_col, current_dist + 1))
                    visited.append((current_row, current_col))

            return min_dist
    
        for i, row in enumerate(mat):
            for j, col in enumerate(row):
                new_mat[i][j] = bfs(i, j)

        return new_mat
