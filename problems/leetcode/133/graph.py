from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(edges: list[list[int]]):
    nodes_dict: dict[int, Node] = {}
    for edge in edges:
        for value in edge:
            if value not in nodes_dict:
                nodes_dict[value] = Node(value, list())
    for value, neighbor in edges:
        nodes_dict[value].neighbors.append(nodes_dict[neighbor])
        nodes_dict[neighbor].neighbors.append(nodes_dict[value])
    return list(nodes_dict.values())

def compareGraphIds(n1, n2, g1=None, g2=None):
    compare = lambda x,y: x == y
    return compareGraphs(n1, n2, g1, g2, compare)

def compareGraphValues(n1, n2, g1=None, g2=None):
    compare = lambda x,y: x.val == y.val
    return compareGraphs(n1, n2, g1, g2, compare)

def compareGraphs(n1, n2, g1=None, g2=None, equal=lambda: True):
    if n1 is None and n2 is None:
        return True
    if n2 is None or n1 is None:
        return False
    if g1 is None:
        g1 = []
    if g2 is None:
        g2 = []
    if n1 in g1 and n2 in g2:
        return True
    if not equal(n1, n2):
        return False
    g1.append(n1)
    g2.append(n2)
    return all(compareGraphValues(nb1, nb2, g1, g2) for nb1, nb2 in zip(n1.neighbors, n2.neighbors))
