
import pytest

from solution import Solution, ListNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((ListNode(-1, ListNode(1, ListNode(2, ListNode(3, ListNode(1))))), 2), ListNode(-1, ListNode(1, ListNode(2, ListNode(1))))),
        ((ListNode(1), 1), None),
        ((ListNode(1, ListNode(2)), 2), ListNode(2)),
    ],
)
def test_solution(test_input, expected):
    assert compare_linked_lists(Solution().removeNthFromEnd(*test_input), expected)

def compare_linked_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return not l1 and not l2
