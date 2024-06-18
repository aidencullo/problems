import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("1 + 1",), 2),
    ((" 2-1 + 2 ",), 3),
    (("(1+(4+5+2)-3)+(6+8)",), 23),
    (("1-(     -2)",), 3),
    (("2147483647",), 2147483647),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.calculate(*test_input)
    assert actual == expected
