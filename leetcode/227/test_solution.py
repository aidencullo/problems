import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("3+2*2",), 7),
    ((" 3/2 ",), 1),
    ((" 3+5 / 2 ",), 5),
    (("14/3*2",), 8),
    (("1-1+1",), 1),
    (("14-3/2",), 13),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.calculate(*test_input)
    assert actual == expected
