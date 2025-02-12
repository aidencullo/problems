import pytest

from solution import Solution, ListNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
    ],
)
def test_single_node(test_input, expected):
    s = Solution()
    assert compare_nodes(s.getIntersectionNode(*test_input), expected)


def test_single_node():
    s = Solution()
    l = ListNode(4, ListNode(4, ListNode(8, ListNode(4, ListNode(5)))))
    r = ListNode(5, ListNode(6, ListNode(1, l.next.next)))
    
    assert s.getIntersectionNode(r, l) == l.next.next
