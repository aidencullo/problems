import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((4, ), 2),
    ((8, ), 2),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.mySqrt(*test_input) == expected
