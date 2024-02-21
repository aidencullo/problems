from solution import TreeNode
from collections import deque
from typing import Optional

class Queue():
    def __init__(self):
        self.d = deque()
        
    def __bool__(self):
        return bool(self.d)

    def push(self, item):
        self.d.append(item)
        
    def pop(self):
        return self.d.popleft()
    

def inOrder(tree: TreeNode):
    if not tree:
        return []
    return inOrder(tree.left) +  [tree.val] + inOrder(tree.right)

def preOrder(tree: TreeNode):
    if not tree:
        return []
    q = Queue()
    q.push(tree)
    nodes = []
    while q:
        node = q.pop()
        nodes.append(node.val)
        if node.left:
            q.push(node.left)
        if node.right:
            q.push(node.right)
    return nodes


def postOrder(tree: TreeNode):
    if not tree:
        return []
    return postOrder(tree.left) + postOrder(tree.right) +  [tree.val]


def makeTree(lst: list[Optional[int]]) -> Optional[TreeNode]:
    if not lst:
        return None
    root: TreeNode = TreeNode(lst.pop(0))
    for item in lst:
        addNode(root, TreeNode(item))
    return root


def countNodes(branch: Optional[TreeNode]) -> int:
    if not branch:
        return 0
    return 1 + countNodes(branch.left) + countNodes(branch.right)


def isPerfect(tree: Optional[TreeNode]) -> int:
    n: int  = 0
    nodes: int = countNodes(tree)
    while 2**n - 1 < nodes:
        n += 1
    return 2**n - 1 == nodes


def addNode(branch: TreeNode, leaf: TreeNode) -> None:
    if not branch.left:
        branch.left = leaf
    elif not branch.right:
        branch.right = leaf
    elif not isPerfect(branch.left):
        addNode(branch.left, leaf)
    elif not isPerfect(branch.right):
        addNode(branch.right, leaf)
    elif height(branch.left) == height(branch.right):
        addNode(branch.left, leaf)
    else:
        addNode(branch.right, leaf)

        
def height(tree: TreeNode) -> None:
    if not tree:
        return 0
    return 1 + max(height(tree.left), height(tree.left))
