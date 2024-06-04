class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.head = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey - 1] = value
        res = []
        while self.head < len(self.stream) and self.stream[self.head]:
            res.append(self.stream[self.head])
            self.head += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
