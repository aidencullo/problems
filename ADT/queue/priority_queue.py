'''
priority queue with min heap

O(log n) enqueue
O(log n) dequeue
'''

import heapq
from dataclasses import dataclass, field

@dataclass
class PriorityQueue:
    items: list[int] = field(default_factory=list)

    def enqueue(self, data: int) -> None:
        heapq.heappush(self.items, -data)

    def dequeue(self) -> str:
        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return -heapq.heappop(self.items)

    def is_empty(self) -> bool:
        return not self.items

    def size(self) -> int:
        return len(self.items)
