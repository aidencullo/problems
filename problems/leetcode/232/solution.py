class MyQueue:

    def __init__(self):
        self.front = []
        self.end = []

    def push(self, x: int) -> None:
        self.end.append(x)

    def pop(self) -> int:
        self._fix_stack()
        return self.front.pop()            

    def peek(self) -> int:
        self._fix_stack()
        return self.front[-1]

    def _fix_stack(self) -> None:
        if not self.front:
            while self.end:
                self.front.append(self.end.pop())

    def empty(self) -> bool:
        return not self.front and not self.end
