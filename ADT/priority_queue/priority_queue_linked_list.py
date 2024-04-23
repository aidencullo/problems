from dataclasses import dataclass, field
from typing import List, Tuple

from dataclasses import dataclass, field

@dataclass
class LinkedListNode:
    name: str
    priority: int
    next = None

@dataclass
class PriorityQueue:
    head: LinkedListNode = None
    num_items: int = 0

    def enqueue(self, name: str, priority: int) -> None:
        self.num_items += 1
        if not self.head:
            self.head = LinkedListNode(name, priority)
            return
        if priority > self.head.priority:
            node = LinkedListNode(name, priority)
            node.next = self.head
            self.head = node
            return
        runner = self.head
        while runner.next and priority <= runner.next.priority:
            runner = runner.next
        node = LinkedListNode(name, priority)
        node.next = runner.next
        runner.next = node

    def dequeue(self) -> str:
        if not self.head:
            raise IndexError('Cannot dequeue from an empty queue')
        self.num_items -= 1
        data = self.head.name
        self.head = self.head.next
        return data

    def is_empty(self) -> bool:
        return not self.head

    def size(self) -> bool:
        return self.num_items
