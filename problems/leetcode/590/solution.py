class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result = []
        stack = []
        next_child = []
        node = root
        while node or stack:
            stack.append(node)
            for child in (node.children or []):
                stack.append(child)
            node = stack.pop()
            result.append(node.val)
        return result
