from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return float('inf')
            if mat[row][col] == 0:
                return 0
            if (row, col) in self.visited:
                return float('inf')
            self.visited.add((row, col))
            return 1 + min(dfs(row + dr, col + dc) for dr, dc in directions)

        self.memo = {}
        self.visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rows = len(mat)
        cols = len(mat[0])
        res = [[0] * cols for __ in range(rows)]
        for row in range(rows):
            for col in range(cols):
                print(res)
                self.visited.clear()
                res[row][col] = dfs(row, col)
        return res
