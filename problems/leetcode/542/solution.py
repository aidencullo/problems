# from collections import deque
# from copy import deepcopy
# from typing import List


# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         width = len(mat[0])
#         height = len(mat)
#         new_mat = deepcopy(mat)

#         def bfs(row, col):
#             min_dist = float('inf')
#             q = deque()
#             q.append((row, col, 0))
#             visited = [(row, col)]

#             while q:
#                 current_row, current_col, current_dist = q.popleft()

#                 if current_row > height - 1 or current_row < 0 or current_col > width - 1 or current_col < 0:
#                     continue

#                 if mat[current_row][current_col] == 0:
#                     min_dist = min(min_dist, current_dist)
#                     continue

#                 current_row += 1
#                 if (current_row, current_col) not in visited:
#                     q.append((current_row, current_col, current_dist + 1))
#                     visited.append((current_row, current_col))
#                 current_row -= 2
#                 if (current_row, current_col) not in visited:
#                     q.append((current_row, current_col, current_dist + 1))
#                     visited.append((current_row, current_col))
#                 current_row += 1
#                 current_col += 1
#                 if (current_row, current_col) not in visited:
#                     q.append((current_row, current_col, current_dist + 1))
#                     visited.append((current_row, current_col))
#                 current_col -= 2
#                 if (current_row, current_col) not in visited:
#                     q.append((current_row, current_col, current_dist + 1))
#                     visited.append((current_row, current_col))

#             return min_dist
    
#         for i, row in enumerate(mat):
#             for j, col in enumerate(row):
#                 new_mat[i][j] = bfs(i, j)

#         return new_mat

# ## someone else's solution
# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         if not mat or not mat[0]:
#             return []

#         m, n = len(mat), len(mat[0])
#         queue = deque()
#         MAX_VALUE = m * n
        
#         # Initialize the queue with all 0s and set cells with 1s to MAX_VALUE.
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] == 0:
#                     queue.append((i, j))
#                 else:
#                     mat[i][j] = MAX_VALUE
        
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
#         while queue:
#             row, col = queue.popleft()
#             for dr, dc in directions:
#                 r, c = row + dr, col + dc
#                 if 0 <= r < m and 0 <= c < n and mat[r][c] > mat[row][col] + 1:
#                     queue.append((r, c))
#                     mat[r][c] = mat[row][col] + 1
        
#         return mat
