class SmallestInfiniteSet:

    def __init__(self):
        self.inf_set = set(range(1, 1001))

    def popSmallest(self) -> int:
        num = min(self.inf_set)
        self.inf_set.remove(num)
        return num
    
    def addBack(self, num: int) -> None:
        self.inf_set.add(num)
