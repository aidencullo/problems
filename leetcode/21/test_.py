import pytest

from solution import ListNode, Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([-9, 3], [5, 7]), [-9, 3, 5, 7]),
        (([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]),
        (([], []), []),
        (([], [0]), [0]),
    ],
)
def test_single_node(test_input, expected):
    # Arrange
    l1, l2 = test_input
    ll1 = buildLL(l1)
    ll2 = buildLL(l2)
    ll_expected = buildLL(expected)
    
    # Act
    ll_actual = Solution().mergeTwoLists(ll1, ll2)

    # Assert
    assert compareLL(ll_actual, ll_expected)


def compareLL(l1, l2):
    while l1 and l2:
        if l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    if l1 or l2:
        return False
    return True


def buildLL(l):
    if not l:
        return None
    head = ListNode(l.pop(0))
    current = head
    for item in l:
        current.next = ListNode(item)
        current = current.next
    return head
