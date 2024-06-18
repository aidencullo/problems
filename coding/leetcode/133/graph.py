from collections import defaultdict
from typing import List

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def buildGraph(edges: List[List[int]], N: int):
    if not edges:
        return None
    def dfs(i):
        if i in visited:
            return nodes[i]

        visited.add(i)
        for j in graph[i]:
            nodes[i].neighbors.append(dfs(j))
        return nodes[i]

    graph = build_raw_graph(edges)
    visited = set()
    nodes = {i: Node(i) for i in range(1, N + 1)}
    head = dfs(1)
    return head


def build_raw_graph(edges):
    graph = defaultdict(list)
    for src, dest in edges:
        graph[src].append(dest)
        graph[dest].append(src)
    return graph


def compareGraphByValue(graph_B: Node, graph_A: Node):
    def compareGraphByValueHelper(graph_B: Node, graph_A: Node):
        if not graph_A and not graph_B:
            return True
        if (graph_A, graph_B) in visited:
            return True
        visited.add((graph_A, graph_B))
        if not compareNodes(graph_A, graph_B):
            return False
        for neighbor_B, neighbor_A in zip(graph_A.neighbors, graph_B.neighbors):
            if not compareGraphByValueHelper(neighbor_A, neighbor_B):
                return False
        return True
    visited = set()
    return compareGraphByValueHelper(graph_A, graph_B)


def compareNodes(u, v):
    if not u and not v:
        return True
    if not u or not v:
        return False
    if u.val != v.val:
        return False
    if len(u.neighbors) != len(v.neighbors):
        return False
    return True


def compareGraphById(graph_B: Node, graph_A: Node):
    def compareGraphByIdHelper(graph_B: Node, graph_A: Node):
        if not graph_A and not graph_B:
            return True
        if (graph_A, graph_B) in visited:
            return True
        visited.add((graph_A, graph_B))
        if graph_A != graph_B:
            return False
        for neighbor_B, neighbor_A in zip(graph_A.neighbors, graph_B.neighbors):
            if not compareGraphByIdHelper(neighbor_A, neighbor_B):
                return False
        return True
    visited = set()
    return compareGraphByIdHelper(graph_A, graph_B)
