import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("123", "3"), "12"),
        (("1231", "1"), "231"),
        (("551", "5"), "51"),
    ],
)
def test_solution(test_input, expected):
    assert Solution().removeDigit(*test_input) == expected
