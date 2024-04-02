import copy

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        graph = []
        findGraph(node, graph)
        newGraph = copy.deepcopy(graph)
        return newGraph[0]


def findGraph(n, g):
    if n in g:
        return
    g.append(n)
    for nb in n.neighbors:
        findGraph(nb, g)
