class Node:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
        

class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_first(self, item: int) -> None:
        if not self.head:
            self.head = self.tail = Node(item)
            return
        node = Node(item)
        node.next = self.head
        self.head.prev = node
        self.head = node

    def add_last(self, item: int) -> None:
        if not self.head:
            self.head = self.tail = Node(item)
            return
        node = Node(item)
        self.tail.next = node
        node.prev = self.tail
        self.tail = node

    def remove_first(self) -> None:
        if not self.head:
            return
        self.head = self.head.next
        if not self.head:
            self.tail = None

    def remove_last(self) -> None:
        if not self.tail:
            return
        self.tail = self.tail.prev
        if not self.tail:
            self.head = None

# # test
# ll = DoublyLinkedList()
# ll.add_first(2)
# ll.add_first(1)
# ll.add_first(3)
# assert ll.head.val == 3
# # assert ll.tail.val == 2

# ll.add_first(4)
# assert ll.head.val == 4
# assert ll.tail.val == 2

# ll.add_last(5)
# assert ll.head.val == 4
# assert ll.tail.val == 5

# ll.remove_first()
# assert ll.head.val == 3
# assert ll.tail.val == 5

# ll.remove_last()
# assert ll.head.val == 3
# assert ll.tail.val == 2
