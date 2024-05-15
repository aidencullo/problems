import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((0b00000000000000000000000000001011, ), 3),
        ((0b00000000000000000000000010000000, ), 1),
    ],
)
def test_solution(test_input, expected):
    assert Solution().hammingWeight(*test_input) == expected
