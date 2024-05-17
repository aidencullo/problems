from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                if node.left:
                    if node.right:
                        stack.append(node.right)
                    node = node.left
                else:
                    if node.right:
                        node = node.right
                    else:
                        node = node.left                        
            u = stack.pop()
            res.append(u.val)
            if not stack:
                break
            v = stack.pop()
            while v.right == u or v.left == u:
                res.append(v.val)
                if not stack:
                    break
                u = v
                v = stack.pop()
            else:
                node = v                
        return res
