import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((121,), True),
    ((-121,), False),
    ((10,), False),
    ((-101,), False),
    ((0,), True),
    ((-1,), False),
    ((12321,), True),
    ((12345678987654321,), True),
    ((123456789876543210,), False),
    ((1234567898765432109,), False),
    ((12345678987654321098,), False),
    ((123456789876543210987,), False),
    ((1234567898765432109876,), False),
    ((12345678987654321098765,), False),
    ((123456789876543210987654,), False),
    ((1234567898765432109876543,), False),
    ((12345678987654321098765432,), False),
])
def test_solution(test_input, expected):
    assert Solution().isPalindrome(*test_input) == expected
