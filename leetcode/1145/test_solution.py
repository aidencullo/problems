import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([9,9], [[1,1,1]], [2,2]), 2),
    (([2,5], [[3,0,5],[1,2,10]], [3,2]), 14),
    (([2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]), 11),
])
def test_solution(test_input, expected):
    assert Solution().shoppingOffers(*test_input) == expected
