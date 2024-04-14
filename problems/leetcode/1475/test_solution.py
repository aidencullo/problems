import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([8,4,6,2,3],), [4,2,4,2,3]),
    (([1,2,3,4,5],), [1,2,3,4,5]),
    (([10,1,1,6],), [9,0,1,6]),
])
def test_solution(test_input, expected):
    assert Solution().finalPrices(*test_input) == expected
