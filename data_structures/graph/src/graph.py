from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass, field


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def add_vertex(self, vertex):
        self.vertices[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        self.check_contains(from_vertex)
        self.check_contains(to_vertex)
        self.vertices[from_vertex].append(to_vertex)

    def check_contains(self, vertex):
        if vertex not in self.vertices:
            raise ValueError(f"Vertex {vertex} not in graph")

    def get_neighbors(self, vertex):
        return self.vertices[vertex]
