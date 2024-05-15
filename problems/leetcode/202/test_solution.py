import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((19, ), True),
        ((2, ), False),
    ],
)
def test_solution(test_input, expected):
    assert Solution().isHappy(*test_input) == expected
