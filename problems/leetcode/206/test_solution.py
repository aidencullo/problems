import pytest

from solution import Solution

from ll import ListNode, list_to_ll, ll_to_list

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3,4,5],), [5,4,3,2,1]),
        (([1,2,3],), [3,2,1]),
    ]
)
def testSolution(test_input, expected):
    ll = list_to_ll(*test_input)
    actual_ll = Solution().reverseList(ll)
    actual_lst = ll_to_list(actual_ll)
    assert actual_lst == expected
