import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([3,2,4,1],), [3,4,2,3,1]),
])
def test_solution(test_input, expected):
    assert Solution().pancakeSort(*test_input) == expected
