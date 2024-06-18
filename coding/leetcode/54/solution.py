from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        self.res = []
        n = len(matrix)
        m = len(matrix[0])
        direction = [(0,1), (1,0), (0,-1), (-1,0)]
        def dfs(i, j, d=0):
            if 0 <= i < n and 0 <= j < m and matrix[i][j] != None:
                self.res.append(matrix[i][j])
                matrix[i][j] = None
                for k in range(4):
                    dr, dc = direction[(d+k)%4]
                    dfs(i+dr, j+dc, (d+k)%4)
        dfs(0,0)
        return self.res
