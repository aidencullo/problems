import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    ((1,), [[1]]),
    ((2,), [[1], [1, 1]]),
    ((3,), [[1], [1, 1], [1, 2, 1]]),
    ((4,), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]),
    ((5,), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
])
def test_solution(test_input, expected):
    assert Solution().generate(*test_input) == expected
