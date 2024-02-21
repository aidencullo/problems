from util import Stack

"""
pop - O(1) time
peek - O(1) time
push - O(n) time
isempty - O(1) time
"""
class MyQueue:

    def __init__(self):
        self.main = Stack()
        self.helper = Stack()

    def push(self, x: int) -> None:
        migrate(self.main, self.helper)
        self.main.push(x)
        migrate(self.helper, self.main)
        
    def pop(self) -> int:
        return self.main.pop()

    def peek(self) -> int:
        return self.main.peek()

    def isEmpty(self) -> bool:
        return self.main.isEmpty()

def migrate(src, target):
    while src:
        target.push(src.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
