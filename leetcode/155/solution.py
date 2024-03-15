class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if val <= self.min_stack[-1]:
                self.min_stack.append(val)
        self.main_stack.append(val)

    def pop(self) -> None:
        top = self.main_stack.pop()
        if top == self.min_stack[-1]:
            self.min_stack.pop()
        return top

    def top(self) -> int:
        return self.main_stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# # ex
# minStack = MinStack()
# minStack.push(0)
# minStack.push(1)
# minStack.push(0)
# minStack.pop()
# minStack.pop()
# minStack.top()
