class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: list[list[int]]) -> 'Node':
        k = len(grid) // 2
        if len(grid) == 1:
            return Node(grid[0][0] == 1, True)
        lu = self.construct([row[:k] for row in grid[:k]])
        ru = self.construct([row[k:] for row in grid[:k]])
        lb = self.construct([row[:k] for row in grid[k:]])
        rb = self.construct([row[k:] for row in grid[k:]])
        if lu.isLeaf and ru.isLeaf and lb.isLeaf and rb.isLeaf and lu.val == ru.val == lb.val == rb.val:
            return Node(lu.val, True)
        return Node(True, False, lu, ru, lb, rb)
