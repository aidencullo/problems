import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.heap = list(range(1, 1001))

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.removed.add(num)
        return num
    
    def addBack(self, num: int) -> None:
        if num in self.removed:
            self.removed.remove(num)
            heapq.heappush(self.heap, num)
