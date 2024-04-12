class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def delete(self, data: int) -> None:
        if self.head.data == data:
            self.head = self.head.next
            return
        runner = self.head
        while runner.next:
            if runner.next.data == data:
                runner.next = runner.next.next
                return
            runner = runner.next
