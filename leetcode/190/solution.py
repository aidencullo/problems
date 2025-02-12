from collections import deque

class Solution:
    def reverseBits(self, n: int) -> int:
        q = deque()
        for i in range(32):
            q.append(n & 1)
            n >>= 1
        for i in range(32):
            n <<= 1
            n |= (q.popleft())
        return n
