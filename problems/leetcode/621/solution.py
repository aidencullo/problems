# time: O(N)
# space: O(1)

from typing import List
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks) # O(N)
        h = MaxHeap()
        for count in task_counter.values(): # O(1)
            h.insert(count) # O(1)
        q = deque()
        t = 0
        while q or h:
            if q:
                count, next_time = q[0]
                if next_time <= t:
                    q.popleft()
                    h.insert(count)                    
            if h:
                count = h.extract() # O(1)
                if count > 1:
                    q.append((count - 1, t + n + 1)) # O(1)
            t += 1                             
        return t

import heapq
from dataclasses import dataclass, field

@dataclass
class MaxHeap:
    items: list[int] = field(default_factory=list)

    def insert(self, data: int) -> None:
        heapq.heappush(self.items, -data)

    def extract(self) -> str:
        if self.is_empty():
            raise IndexError('extract from empty heap')
        return -heapq.heappop(self.items)

    def is_empty(self) -> bool:
        return not self.items

    def __len__(self) -> int:
        return len(self.items)
