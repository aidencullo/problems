import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((5, ), [0, 1, 1, 2, 1, 2]),
        ((2, ), [0, 1, 1]),
        ((0, ), [0]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().countBits(*test_input) == expected
