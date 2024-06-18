import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([0], 23), [2, 3]),
    (([9,9,9,9,9,9,9,9,9,9], 1), [1,0,0,0,0,0,0,0,0,0,0]),
    (([1, 2, 0, 0], 34), [1, 2, 3, 4]),
    (([2, 7, 4], 181), [4, 5, 5]),
    (([2, 1, 5], 806), [1, 0, 2, 1]),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.addToArrayForm(*test_input) == expected
