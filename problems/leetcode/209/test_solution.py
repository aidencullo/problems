import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((7, [2,3,1,2,4,3]), 2),
    ((4, [1,4,4]), 1),
    ((11, [1,1,1,1,1,1,1,1]), 0),
    ((11, [1,2,3,4,5]), 3),
    ((15, [1,2,3,4,5]), 5),
])
def test_solution(test_input, expected):
    assert Solution().minSubArrayLen(*test_input) == expected
