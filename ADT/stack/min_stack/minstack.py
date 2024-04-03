class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        if self.get_min() > x:
            self.min_stack.append(x)

    def pop(self) -> None:
        if not self.stack:
            return None
        top = self.stack.pop()
        if top == self.get_min():
            self.min_stack.pop()
        return top

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def get_min(self) -> int:
        return self.min_stack[-1] if self.min_stack else None
