import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
    ],
)
def test_solution(test_input, expected):
    assert Solution().findDuplicate(*test_input) == expected
