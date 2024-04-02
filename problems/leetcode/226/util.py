from collections import deque
import math

from solution import TreeNode
 
def makeTree(l: list[int]) -> TreeNode:
    if not l:
        return None

    level: int = math.ceil(math.log2(len(l) + 1) - 1)

    left = []
    right = []
    
    for i in range(1, level+1):
        start: int = 2**i - 1
        width: int = 2 ** (i-1)
        left += l[start: start+width]
        right += l[start+width: start+2*width]

    head: TreeNode = TreeNode(l[0],
                              makeTree(left),
                              makeTree(right))
    return head

# assume tree is balanced
def compareTree(t1, t2) -> bool:
    if not t1 and not t2:
        return True
    if t1 and not t2:
        return False
    if not t1 and t2:
        return False
    if t1.val != t2.val:
        return False
    return (compareTree(t1.left, t2.left)
            and compareTree(t1.right, t2.right))
