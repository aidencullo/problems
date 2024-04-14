import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([4,1,2], [1,3,4,2]), [-1,3,-1]),
    (([2,4], [1,2,3,4]), [3,-1])
])
def test_solution(test_input, expected):
    assert Solution().nextGreaterElement(*test_input) == expected
