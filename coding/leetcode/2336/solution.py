class SmallestInfiniteSet:

    def __init__(self):
        self.hash_set = set()

    def popSmallest(self) -> int:
        i = 1
        while i in self.hash_set:
            i += 1
        self.hash_set.add(i)
        return i

    def addBack(self, num: int) -> None:
        if num in self.hash_set:
            self.hash_set.remove(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
