import pytest

from solution import Solution
from solution import ListNode

@pytest.mark.parametrize("test_input, expected", [
    ((ListNode(3, ListNode(5)), 1, 2), ListNode(5, ListNode(3))),
    ((ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2, 4), ListNode(1, ListNode(4, ListNode(3, ListNode(2, ListNode(5)))))),
    ((ListNode(5), 1, 1), ListNode(5)),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert compare_LL(sol.reverseBetween(*test_input), expected)

def compare_LL(l1, l2):
    if not l1 and not l2:
        return True
    if not l1 or not l2:
        return False
    if l1.val != l2.val:
        return False
    return compare_LL(l1.next, l2.next)
