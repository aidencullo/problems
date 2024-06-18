import pytest

from solution import Solution
from list_node import ListNode

def test_solution():
    input_list = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4))))))
    expected = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    assert compare_linked_lists(Solution().removeDuplicates(input_list), expected)


def test_solution_geeks():
    input_list = ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2, ListNode(2))))))
    expected = ListNode(2)
    assert compare_linked_lists(Solution().removeDuplicates(input_list), expected)


def compare_linked_lists(list1: ListNode, list2: ListNode) -> bool:
    while list1 and list2:
        if list1.data != list2.data:
            return False
        list1 = list1.next
        list2 = list2.next
    return list1 is None and list2 is None
