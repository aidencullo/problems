from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field

from node import Node

class Graph:
    def __init__(self):
        self._vertices = {}
    
    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.check_contains(from_vertex)
        self.check_contains(to_vertex)
        self._vertices[from_vertex].append(to_vertex)

    def check_contains(self, vertex):
        if vertex not in self._vertices:
            raise ValueError(f"Vertex {vertex} not in graph")

    def get_neighbors(self, vertex):
        return self._vertices[vertex]


class NodeGraph(Graph):

    def __init__(self, adjacency_list=None):
        super().__init__()
        if adjacency_list is not None:
            for vertex, neighbors in adjacency_list.items():
                self.add_vertex(vertex)
                for neighbor in neighbors:
                    self.add_vertex(neighbor)
                    self.add_edge(vertex, neighbor)

    def add_vertex(self, vertex):
        if vertex not in self._vertices:
            self._vertices[vertex] = Node(vertex)

    def add_edge(self, from_vertex, to_vertex):
        self.check_contains(from_vertex)
        self.check_contains(to_vertex)
        self._vertices[from_vertex].add_neighbor(self._vertices[to_vertex])

    def get_neighbors(self, vertex):
        return [node.val for node in self._vertices[vertex].neighbors]

    def get_root(self):
        return list(self._vertices.values())[0]
