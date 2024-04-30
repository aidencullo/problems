import pytest

from solution import Solution
from tree import Node


def test_simple_solution():
    input_list = Node(2, Node(1), Node(3))
    expected = build_dll([1, 2, 3])
    result = Solution().bToDLL(input_list)
    assert compare_linked_lists(result, expected)


def test_solution():
    input_list = Node(5, Node(1, Node(0), Node(2)), Node(10, Node(7), Node(12)))
    expected = build_dll([0, 1, 2, 5, 7, 10, 12])
    result = Solution().bToDLL(input_list)
    assert compare_linked_lists(result, expected)


def test_geeksforgeeks():
    input_list = Node(5, Node(1, Node(0), Node(2)), Node(10, Node(7)))
    expected = build_dll([0, 1, 2, 5, 7, 10])
    result = Solution().bToDLL(input_list)
    assert compare_linked_lists(result, expected)

def build_dll(arr: list) -> Node:
    head = Node(0)
    runner = head
    while arr:
        node = Node(arr.pop())
        node.right = runner.right
        node.left = runner
        runner.right = node
        if node.right:
            node.right.left = node
    return head.right

    
def compare_linked_lists(list1: Node, list2: Node) -> bool:
    while list1 and list2:
        if list1.data != list2.data:
            return False
        list1 = list1.right
        list2 = list2.right
    return list1 is None and list2 is None


def print_DLL(head: Node) -> bool:
    runner = head
    while runner:
        print(runner.data)
        runner = runner.right
