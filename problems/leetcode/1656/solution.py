class OrderedStream:

    def __init__(self, n: int):
        self.stream = [None] * n
        self.head = 0

    def insert(self, idKey: int, value: str) -> list[str]:
        self.stream[idKey - 1] = value
        while self.head < len(self.stream) and self.stream[self.head]:
            self.head += 1
        return self.stream[idKey - 1:self.head]
