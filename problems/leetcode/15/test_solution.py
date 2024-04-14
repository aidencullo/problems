import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([-1,0,1,2,-1,-4],), [[-1,-1,2],[-1,0,1]]),
    (([0,1,1],), []),
    (([0,0,0],), [[0,0,0]]),
    (([0,0,0,0],), [[0,0,0]]),
])
def test_solution(test_input, expected):
    assert Solution().threeSum(*test_input) == expected
