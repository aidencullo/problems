# primitive linked list
# i didn't know how to make a pointer to another node from one node

from dataclasses import dataclass, field


class Node:
    next = None
    def __init__(self, value):
        self.value = value
        
class LL:
    head: Node = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.head.next = None
            return
        current = self.head
        while current.next:
            print(f'{current}')
            current = current.next
        current.next = new_node

    
    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(current.value)
            current = current.next
        return str(values)

# ll = LL()
# ll.append(1)
# ll.append(1)
# ll.append(1)
# print(f'{ll}')

# # more proper implementation
# # A single node of a singly linked list
# class Node:
#     # constructor
#     def __init__(self, data, next=None): 
#         self.data = data
#         self.next = next

#     def __repr__(self):
#         return f'{self.data=}'

# def print_nodes(head):
#     current = head
#     while current.next:
#         print(f'{current}')
#         current = current.next
#     print(f'{current}')
        
    
# # Creating a single node
# another_node = Node(3)
# a_node = Node(2, another_node)
# head = Node(1, a_node)

# print_nodes(head)
