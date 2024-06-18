from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(row, col):
            if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]):
                return
            if image[row][col] != start_color:
                return
            image[row][col] = color
            for dr, dc in directions:
                dfs(row + dr, col + dc)                

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        start_color = image[sr][sc]
        if start_color != color:
            dfs(sr, sc)
        return image
