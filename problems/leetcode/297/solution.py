# bfs

# time complexity: O(n)
# space complexity: O(n)

from collections import deque
import re

from tree import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = []
        q = deque()
        if root:
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
        data = re.sub('[][]', "", data)
        data = [int(c) if c != "None" else None for c in data.split(", ")]
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












# dfs

# time complexity: O(n)
# space complexity: O(n)

from collections import deque
import re

from tree import TreeNode

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = ""
        def dfs(node: TreeNode):
            nonlocal serial
            if node:
                serial += ' ' + str(node.val)
                dfs(node.left)
                dfs(node.right)
            else:
                serial += ' ' + 'None'
        dfs(root)
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = self.extract_list(data)
        self.i = 0
        def dfs():
            if data[self.i] is None:
                return None
            node = TreeNode(data[self.i])
            self.i += 1
            node.left = dfs()
            self.i += 1
            node.right = dfs()
            return node
        return dfs()
        
    def extract_list(self, data):        
        return [int(c) if c != 'None' else None for c in data.split()]
