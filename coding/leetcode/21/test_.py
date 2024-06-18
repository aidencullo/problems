import pytest

from solution import ListNode, Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
        ),
         ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))),
    ],
)
def test_solution(test_input, expected):
    assert compare_lists(Solution().mergeTwoLists(*test_input), expected)

def compare_lists(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return not l1 and not l2
