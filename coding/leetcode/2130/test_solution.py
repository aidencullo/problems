import pytest
from solution import ListNode, Solution

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

@pytest.mark.parametrize("values, expected", [
    ([5, 4, 2, 1], 6),
    ([4, 2, 2, 3], 7),
    ([1, 100000], 100001),
])
def test_pairSum(values, expected):
    head = create_linked_list(values)
    solution = Solution()
    assert solution.pairSum(head) == expected
