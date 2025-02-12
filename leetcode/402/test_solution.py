import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("1432219", 3), "1219"),
    (("10200", 1), "200"),
    (("10", 2), "0"),
    (("9", 1), "0"),
    (("112", 1), "11"),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.removeKdigits(*test_input) == expected
