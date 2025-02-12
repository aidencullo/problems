from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        if '0000' in deadends:
            return -1

        def children(comb):
            for i in range(4):
                x = int(comb[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield comb[:i] + str(y) + comb[i+1:]
        
        q = deque()
        q.append(['0000', 0])
        visited = set(deadends)
        while q:
            comb, count = q.popleft()
            if comb == target:
                return count
            for child in children(comb):
                if not child in visited:
                    visited.add(child)
                    q.append([child, count + 1])
        return -1
