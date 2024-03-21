import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((4325,), 59),
        ((687,), 75),
    ]
)
def testSolution(test_input, expected):
    assert Solution().splitNum(*test_input) == expected
