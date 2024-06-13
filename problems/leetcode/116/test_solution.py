# File: test_solution.py

import pytest
from solution import Node, Solution

def tree_to_list_with_next(root: 'Optional[Node]') -> list:
    """ Helper function to convert tree to list including next pointers for testing. """
    result = []
    level_start = root
    while level_start:
        current = level_start
        level_start = None
        next_level_first = None
        while current:
            result.append(current.val)
            if not next_level_first:
                next_level_first = current.left
            if current.next:
                result.append("->")
            current = current.next
        result.append("#")
        level_start = next_level_first
    return result

def test_connect():
    solution = Solution()
    
    # Test case 1
    root = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))
    solution.connect(root)
    assert tree_to_list_with_next(root) == [1, "#", 2, "->", 3, "#", 4, "->", 5, "->", 6, "->", 7, "#"]
    
    # Test case 2
    root = None
    solution.connect(root)
    assert tree_to_list_with_next(root) == []

