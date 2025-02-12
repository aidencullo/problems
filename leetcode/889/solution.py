from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        node = TreeNode(preorder.pop(0))
        postorder.pop()
        if preorder:
            left_child = preorder[0]
            right_child = postorder[-1]
            if left_child == right_child:
                node.left = self.constructFromPrePost(preorder, postorder)
            else:
                pre_right = preorder.index(right_child)
                post_left = postorder.index(left_child)
                node.left = self.constructFromPrePost(preorder[:pre_right], postorder[:post_left + 1])
                node.right = self.constructFromPrePost(preorder[pre_right:], postorder[post_left + 1:])
        return node
