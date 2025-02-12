import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (('III',), 3),
    (('IV',), 4),
    (('IX',), 9),
    (('LVIII',), 58),
    (('MCMXCIV',), 1994),
])
def test_solution(test_input, expected):
    assert Solution().romanToInt(*test_input) == expected
