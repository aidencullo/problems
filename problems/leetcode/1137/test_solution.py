import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((4,), 4),
        ((25,), 1389537),
    ],
)
def test_solution(test_input, expected):
    assert Solution().tribonacci(*test_input) == expected
