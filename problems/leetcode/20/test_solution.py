import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("()",), True),
    (("()[]{}",), True),
    (("([)]",), False),
    (("{[]}",), True),
    (("(",), False),
    (("()",), True),
])
def test_solution(test_input, expected):
    sol = Solution().isValid(*test_input)
