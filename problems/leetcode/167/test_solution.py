import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([2,7,11,15], 9), [1,2]),
    (([2,3,4], 6), [1,3]),
    (([2,3,3,4], 6), [1,4]),
])
def test_solution(test_input, expected):
    assert Solution().twoSum(*test_input) == expected
