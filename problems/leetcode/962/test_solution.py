import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([6,0,8,2,1,5],), 4),
    (([9,8,1,0,1,9,4,0,4,1],), 7),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.maxWidthRamp(*test_input)
    assert actual == expected
