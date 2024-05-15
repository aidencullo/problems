import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((6, ), True),
        ((1, ), True),
        ((14, ), False),
        ((7, ), False),
    ],
)
def test_solution(test_input, expected):
    assert Solution().isUgly(*test_input) == expected
