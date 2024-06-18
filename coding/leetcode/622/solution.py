from DoublyLinkedList import DoublyLinkedList        
        
class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.items = DoublyLinkedList()

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.items.add_first(value)
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.items.remove_last()
        self.size -= 1
        return True

    def Front(self) -> int:
        return self.items.tail.val if not self.isEmpty() else -1

    def Rear(self) -> int:
        return self.items.head.val if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
