import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1,2,4,3,5,4,7,2],), 3),
    (([1, 3, 5, 4, 7],), 2),
    (([2, 2, 2, 2, 2],), 5),
])
def test_solution(test_input, expected):
    assert Solution().findNumberOfLIS(*test_input) == expected
