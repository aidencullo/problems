import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 3],), [1, 3, 2]),
    (([3, 2, 1],), [1, 2, 3]),
    (([1, 1, 5],), [1, 5, 1]),
    (([1, 3, 2],), [2, 1, 3]),
])
def test_solution(test_input, expected):
    Solution().nextPermutation(*test_input)
    actual, = test_input
    assert actual == expected
