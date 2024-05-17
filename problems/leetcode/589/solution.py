class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = [grandchild
                  for child in root.children
                  for grandchild in self.preorder(child)]
        return [root.val] + result
