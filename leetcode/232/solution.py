class MyQueue:

    def __init__(self):
        self.main = []
        self.helper = []

    def push(self, x: int) -> None:
        migrate(self.main, self.helper)
        self.main.append(x)
        migrate(self.helper, self.main)
        
    def pop(self) -> int:
        return self.main.pop()

    def peek(self) -> int:
        return self.main[-1]

    def empty(self) -> bool:
        return len(self.main) == 0

def migrate(src, target):
    while src:
        target.append(src.pop())


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
