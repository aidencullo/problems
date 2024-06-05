# https://leetcode.com/problems/find-the-xor-of-numbers-which-appear-twice/
import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [    
    (([1, 2, 1, 3]), 1),
    (([1, 2, 3]), 0),
    (([1, 2, 2, 1]), 3),
])
def test_solution(test_input, expected):
    assert Solution().duplicateNumbersXOR(test_input) == expected
