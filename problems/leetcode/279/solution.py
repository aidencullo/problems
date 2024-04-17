# time O(n^1/2), space O(1)

from collections import deque
import math

class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        q.append(n)
        count = 0
        while q:
            count += 1
            qlen = len(q)
            for __ in range(qlen):
                current = q.popleft()
                max_square = math.floor(math.sqrt(current))
                for i in range(max_square, 0, -1):
                    sq = i ** 2
                    if current-sq == 0:
                        return count
                    if current-sq > 0:
                        q.append(current-sq)
