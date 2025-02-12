import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("Let's take LeetCode contest",), "s'teL ekat edoCteeL tsetnoc"),
        (("Mr Ding",), "rM gniD"),
    ],
)
def test_solution(test_input, expected):
    assert Solution().reverseWords(*test_input) == expected
