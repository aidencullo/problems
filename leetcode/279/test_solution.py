import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((12,), 3),
    ((13,), 2),
    ((1,), 1),
    ((7168,), 4),
])
def test_solution(test_input, expected):
    assert Solution().numSquares(*test_input) == expected
