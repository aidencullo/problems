import pytest

from solution import Solution

@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("aa", True),
        ("aaaa", True),
        (" ", True),
        ("race a car", False),
        ("aba", True),
        ("A man, a plan, a canal: Panama", True),
    ],
)
def test(test_input, expected):
    s = Solution()
    assert s.isPalindrome(test_input) == expected
