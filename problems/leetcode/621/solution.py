# time: O(N)
# space: O(1)

from typing import List
from collections import Counter, deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counter = Counter(tasks)
        max_heap = [-cnt for cnt in task_counter.values()]
        heapq.heapify(max_heap)

        q = deque()
        t = 0
        while q or max_heap:
            t += 1
            if q and q[0][1] < t:
                heapq.heappush(max_heap, q.popleft()[0])
            if max_heap:
                count = 1 + heapq.heappop(max_heap)
                if count:
                    q.append((count, t + n))
        return t
