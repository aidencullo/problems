import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.removed = set()
        self.heap = list(range(1, 10001))
        heapq.heapify(self.heap)

    def popSmallest(self) -> int:
        num = heapq.heappop(self.heap)
        self.removed.add(num)
        return num
    
    def addBack(self, num: int) -> None:
        if num not in self.removed:
            self.removed.add(num)
            heapq.heappush(self.heap, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
