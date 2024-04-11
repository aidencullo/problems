from collections import deque
import re

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x=0, left=None, right=None):
#         self.val = x
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "[]"
        serial = []
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            serial.append(node.val) if node else serial.append(None)
            if node:
                q.append(node.left)
                q.append(node.right)
        return str(serial)
                

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "[]":
            return None
        my_new_string = re.sub('[][]', "", data)
        data = [int(c) if c != "None" else None for c in my_new_string.split(", ")]
        i = 0
        root = TreeNode(data[i])
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                i += 1
                node.left = TreeNode(data[i]) if not data[i] is None else None
                i += 1
                node.right = TreeNode(data[i]) if not data[i] is None else None
                q.append(node.left)
                q.append(node.right)
        return root
            

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
