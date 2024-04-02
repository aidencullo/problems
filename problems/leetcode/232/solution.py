from util import Stack

"""
pop - O(1) time
peek - O(1) time
push - O(n) time
isempty - O(1) time
"""
class MyQueue:

    def __init__(self):
        self.left = Stack()
        self.right = Stack()

    def push(self, x: int) -> None:
        self.left.push(x)
        
    def pop(self) -> int:
        if self.right:
            return self.right.pop()
        migrate(self.left, self.right)
        return self.right.pop()

    def peek(self) -> int:
        if self.right:
            return self.right.peek()
        migrate(self.left, self.right)
        return self.right.peek()

    def isEmpty(self) -> bool:
        return self.left.isEmpty() and self.right.isEmpty()

def migrate(src, target):
    while src:
        target.push(src.pop())

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
