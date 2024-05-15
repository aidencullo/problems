import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((["abc","car","ada","racecar","cool"],), "ada"),
    ],
)
def test_solution(test_input, expected):
    assert Solution().firstPalindrome(*test_input) == expected
