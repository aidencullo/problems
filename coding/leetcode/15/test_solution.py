import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([-1,0,1,2,-1,-4],), [[-1,-1,2],[-1,0,1]]),
    (([0,1,1],), []),
    (([0,0,0],), [[0,0,0]]),
    (([0,0,0,0],), [[0,0,0]]),
    (([-2,0,0,2,2],), [[-2,0,2]]),
    (([1,1,-2],), [[-2,1,1]]),
])
def test_solution(test_input, expected):
    assert compare(Solution().threeSum(*test_input), expected)

def compare(a, b):
    return sorted(a) == sorted(b)
