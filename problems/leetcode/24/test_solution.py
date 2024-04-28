import pytest

from solution import Solution, ListNode

def test_solution():
    input_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    expected = ListNode(2, ListNode(1, ListNode(4, ListNode(3))))
    assert compare_linked_lists(Solution().swapPairs(input_list), expected)

def compare_linked_lists(list1: ListNode, list2: ListNode) -> bool:
    if not list1 and not list2:
        return True
    if not list1 or not list2:
        return False
    return compare_linked_lists(list1.next, list2.next)
    
