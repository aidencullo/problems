# R�mov� Dups! Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed? Hints: #9, #40

##########

class Node:
    next = None

    def __init__(self, data):
        self.data = data

    def __eq__(self, other):
        if not other:
            return False
        return self.data == other.data

class LinkedList:
    head: Node = None

    def __init__(self, numbers: list=None):
        if numbers is None:
            numbers = []
        for number in numbers:
            self.add(number)

    def __eq__(self, other):
        if not other:
            return False
        return sorted(self.to_list()) == sorted(other.to_list())

    def __repr__(self):
        return f'Linked List: {self.to_list()}'
    
    def to_list(self):
        items = []
        current = self.head
        while current:
            items.append(current.data)
            current = current.next
        return items

    def add(self, number):
        new_node = Node(number)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete(self, number) -> bool:
        if not self.head:
            return False
        if self.head.data == number:
            self.head = self.head.next
            return True
        current = self.head
        while current and current.next:
            if current.next.data == number:
               current.next = current.next.next
               return True
            current = current.next
        return False

# ########### O(n) time and space
    
# def solution(ll: LinkedList) -> LinkedList:
#     hash_map = []
#     node = Node(-1)
#     node.next = ll.head
#     if not node.next:
#         return ll
#     while node.next:
#         if node.next.data in hash_map:
#             node.next = node.next.next
#         else:
#             hash_map.append(node.next.data)
#             node = node.next
#     return ll

########### O(n^2) time and O(1) space
    
def solution(ll: LinkedList) -> LinkedList:
    hash_map = []
    node = Node(-1)
    node.next = ll.head
    if not node.next:
        return ll
    while node.next:
        runner = node.next
        while runner.next:
            if runner.next == node.next:
                runner.next = runner.next.next
            else:
                runner = runner.next
        node = node.next
    return ll

import pytest

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((LinkedList([1, 2, 4]),), LinkedList([1, 2, 4])),
        ((LinkedList([]),), LinkedList([])),
        ((LinkedList([1, 2, 2, 4]),), LinkedList([1, 2, 4])),
        ((LinkedList([1, 2, 2, 2, 4, 4]),), LinkedList([1, 2, 4])),
        ((LinkedList([1, 2, 2, 2, 4, 4, 1, 1, 2]),), LinkedList([2, 1, 4])),
    ],
)
def test(test_input, expected):
    assert solution(*test_input) == expected


def test_1():
    ll = LinkedList()
    ll.add(1)
    ll.add(1)
    ll.add(1)
    assert ll.delete(1)
    assert ll.delete(1)
    assert ll.delete(1)
    assert not ll.delete(1)
    assert not ll.delete(1)
    assert not ll.delete(1)
