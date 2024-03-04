from __future__ import annotations

from dataclasses import dataclass, field

@dataclass(frozen=True, slots=True)
class Node:
    val: int = 0
    neighbors: list[Node] = field(default_factory=list)

    def add_neighbor(self, node: Node):
        self.neighbors.append(node)
