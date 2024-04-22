'''
priority queue with min heap

O(log n) enqueue
O(log n) dequeue
'''

import heapq
from dataclasses import dataclass, field
from typing import List, Tuple

@dataclass
class PriorityQueue:
    items: List[Tuple[int, str]] = field(default_factory=list)

    def enqueue(self, name: str, priority: int) -> None:
        heapq.heappush(self.items, (-priority, name))

    def dequeue(self) -> str:
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return heapq.heappop(self.items)[1]

    def is_empty(self) -> bool:
        return not self.items

    def size(self) -> int:
        return len(self.items)
