# An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

# You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

# To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

# Return the modified image after performing the flood fill.


# ## O(n) time O(n) space ACCEPTED
# from typing import List
# from collections import deque

# import numpy as np

# class Solution:
#     def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
#         q = deque()
#         to_change = []
#         start = (sr, sc)
#         image_array = np.array(image)
#         start_color = image_array[start]
#         directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


#         if validSquare(image_array, start, start_color, to_change):
#             q.append(start)
#             to_change.append(start)
                
#         while q:
#             current: tuple(int, int) = q.popleft()

#             for direction in directions:
#                 updated = tuple(np.add(current, direction))
#                 if validSquare(image_array, updated, start_color, to_change):
#                     q.append(updated)
#                     to_change.append(updated)


#         for indices in to_change:
#             image_array[indices] = color

#         return image_array.tolist()


# def validSquare(image: np.ndarray, index: tuple[int, int], color: int, to_change):
#     if not onImage(image, index):
#         return False
#     if image[index] != color:
#         return False
#     if index in to_change:
#         return False
#     return True

# def onImage(image: np.ndarray, index: tuple[int, int]):
#     x, y = index
#     N, M = image.shape
#     return 0 <= x < N and 0 <= y < M


## based off someone else's solution!
## O(n) time O(n) space (?)
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target_color: int = color
        start_color = image[sr][sc]
        if start_color == target_color:
            return image
        dfs(image, sr, sc, start_color, target_color)
        return image

def onImage(image: list[list[int]], x: int, y: int):
    N = len(image)
    M = len(image[0])
    return 0 <= x < N and 0 <= y < M

def dfs(lst: list[list[int]], x: int, y: int, start: int, target: int):
    if not onImage(lst, x, y):
        return
    if lst[x][y] == start:
        lst[x][y] = target
        dfs(lst, x+1, y, start, target)
        dfs(lst, x, y+1, start, target)
        dfs(lst, x-1, y, start, target)
        dfs(lst, x, y-1, start, target)
        
