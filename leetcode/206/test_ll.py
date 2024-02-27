import pytest

from ll import ListNode, list_to_ll, ll_to_list


def test_list_to_ll():
    lst = [1,2,3,4]
    actual = list_to_ll(lst)
    assert actual.val == 1
    assert actual.next.val == 2
    assert actual.next.next.val == 3


def test_list_to_ll_empty():
    lst = []
    actual = list_to_ll(lst)
    assert actual is None


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((ListNode(1, ListNode(2, ListNode(3))),), [1,2,3]),
    ]
)
def test_ll_to_list(test_input, expected):
    assert ll_to_list(*test_input) == expected
