from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))


"""
INPUT

tree
- bst?
- order?
- balanced?
- complete?
"""


"""
INPUT CONSTRAINTS

- size
- values
- size of values
- null root? yes

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000
"""

"""
GOAL

- find min depth
- smallest path from root to leaf node
"""

"""
EXAMPLES

ex 1:

 1
2 3

-> 2


ex 2:

  1
 2 3
    6

-> 3

ex 3 -- edge case:

  1

-> 1

ex 4 -- edge case:

  

-> 0
"""

"""

APPROACH

base case: if node is null, return 0

inductive case: return 1 + min path of left and right child

would you like me to elaborate on this algorithm first or begin to implement it?

"""
