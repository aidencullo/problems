from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def height(tree: TreeNode) -> None:
    if not tree:
        return 0
    return 1 + max(height(tree.left), height(tree.right))
