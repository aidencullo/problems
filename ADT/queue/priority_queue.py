'''
naive implementation of a priority queue

O(n) enqueue
O(1) dequeue
'''

from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Node:
    data: str
    priority: int

@dataclass
class PriorityQueue:
    items: list[Node] = field(default_factory=list)

    def enqueue(self, data: str, priority: int) -> None:
        i = 0
        while i < len(self.items) and priority > self.items[i].priority:
            i += 1
        self.items.insert(i, Node(data, priority))

    def dequeue(self) -> str:
        return self.items.pop().data

    def is_empty(self) -> bool:
        return not self.size()

    def size(self) -> int:
        return len(self.items)
