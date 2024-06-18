import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((1, 6, 3), 1),
    ((2, 6, 7), 6),
    ((2, 5, 10), 1),
    ((1, 2, 3), 0),
    ((30, 30, 500), 222616187),
])
def test_solution(test_input, expected):
    assert Solution().numRollsToTarget(*test_input) == expected
