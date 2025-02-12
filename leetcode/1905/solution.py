class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if (r, c) in seen:
                return
            if grid2[r][c] == 0:
                return
            seen.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                dfs(r + dr, c + dc)

        def negative_dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return
            if (r, c) in seen:
                return
            if grid2[r][c] == 0:
                return
            grid2[r][c] = 0            
            seen.add((r, c))
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                negative_dfs(r + dr, c + dc)
        
        seen = set()
        m = len(grid2)
        n = len(grid2[0])
        subislands = 0
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid1[i][j] == 0:
                    negative_dfs(i, j)

        seen = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in seen and grid2[i][j] == 1:
                    dfs(i, j)
                    subislands += 1
        return subislands
