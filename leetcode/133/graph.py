from collections import defaultdict

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(edges: list[list[int]]):
    nodes_dict: dict[int, Node] = {}
    for edge in edges:
        value, neighbor = edge
        if value not in nodes_dict:
            nodes_dict[value] = Node(value, set())
        if neighbor not in nodes_dict:
            nodes_dict[neighbor] = Node(neighbor, set())
    for edge in edges:
        value, neighbor = edge
        nodes_dict[value].neighbors.add(nodes_dict[neighbor])
    return list(nodes_dict.values())[0]

def compareGraphsId(g1, g2):
    pass

def compareGraphsValue(g1, g2):
    pass
