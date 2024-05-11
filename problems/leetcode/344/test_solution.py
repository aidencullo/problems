import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((["h","e","l","l","o"],), ["o","l","l","e","h"]),
    ((["H","a","n","n","a","h"],), ["h","a","n","n","a","H"]),
])
def test_solution(test_input, expected):
    test_input, = test_input
    Solution().reverseString(test_input)
    assert test_input == expected
