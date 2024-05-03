import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((3,), [1,3,3,1]),
    ((0,), [1]),
    ((1,), [1,1]),
    ((2,), [1,2,1]),
    ((15,), [1,15,105,455,1365,3003,5005,6435,6435,5005,3003,1365,455,105,15,1]),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.getRow(*test_input) == expected
