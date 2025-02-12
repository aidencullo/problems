import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("ccaccjp", "fwosarcwge"), 1399),
        (("sea", "eat"), 231),
        (("delete", "leet"), 403),
    ]
)
def testSolution(test_input, expected):
    assert Solution().minimumDeleteSum(*test_input) == expected
