import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((3,), 2),
    ((0,), 0),
    ((1,), 1),
    ((2,), 1),
    ((15,), 610),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.fib(*test_input) == expected
