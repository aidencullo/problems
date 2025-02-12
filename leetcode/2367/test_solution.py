import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([0,1,4,6,7,10], 3), 2),
    (([4,5,6,7,8,9], 2), 2),
    
])
def test_solution(test_input, expected):
    assert Solution().arithmeticTriplets(*test_input) == expected
