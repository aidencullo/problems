import pytest
from typing import List, Optional

from solution import Solution
from list_node import ListNode

@pytest.mark.parametrize("test_input, expected", [
    (([[1,4,5],[1,3,4],[2,6]],), [1,1,2,3,4,4,5,6]),
    (([],), []),
    (([[1,4,5],[1,3,4],[2,6],[7,8,9],],), [1,1,2,3,4,4,5,6,7,8,9]),
    (([[]],), []),
])
def test_solution(test_input, expected):
    list_input = make_list_nodes(*test_input)
    list_expected = make_list_node(expected)
    sol = Solution()
    actual = sol.mergeKLists(list_input)
    assert compare_list_nodes(actual, list_expected)

def compare_list_nodes(list_node_a, list_node_b):
    runner_a = list_node_a
    runner_b = list_node_b
    while runner_a and runner_b:
        if runner_a.val != runner_b.val:
            return False
        runner_a = runner_a.next
        runner_b = runner_b.next
    if runner_a or runner_b:
        return False
    return True

def make_list_nodes(lsts) -> List[ListNode]:
    return [make_list_node(lst) for lst in lsts]

def make_list_node(lst) -> ListNode:
    list_node = ListNode(0)
    for item in lst:
        insert(list_node, item)
    return list_node.next

def insert(list_node: Optional[ListNode], item: int) -> None:
    while list_node.next:
        list_node = list_node.next
    list_node.next = ListNode(item)
    
def print_list_nodes(list_of_list_nodes: List[Optional[ListNode]]) -> None:
    for node in list_of_list_nodes:
        print_list_node(node)

def print_list_node(list_node: Optional[ListNode]) -> None:
    runner = list_node
    while runner:
        print(runner.val)
        runner = runner.next
