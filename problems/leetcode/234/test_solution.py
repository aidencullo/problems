import pytest

from solution import Solution, ListNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((ListNode(1, ListNode(2, ListNode(2, ListNode(1)))),), True),
        ((ListNode(1, ListNode(2)),), False),
        ((ListNode(1),), True),
    ],
)
def test_solution(test_input, expected):
    assert Solution().isPalindrome(*test_input) == expected
