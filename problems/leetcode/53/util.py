from collections import deque

class Stack:

    def __init__(self):
        self.items = deque()

    def __bool__(self):
        return bool(self.items)

    def push(self, x: int) -> None:
        self.items.append(x)
        
    def pop(self) -> int:
        return self.items.pop()

    def peek(self) -> int:
        top: int = self.items.pop()
        self.items.append(top)
        return top

    def isEmpty(self) -> bool:
        return not self.items
