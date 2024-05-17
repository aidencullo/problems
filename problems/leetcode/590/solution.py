class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return []
        if not root.children:
            return [root.val]
        result = [grandchild
                  for child in root.children
                  for grandchild in self.postorder(child)]
        return result + [root.val]
