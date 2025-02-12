import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("pvjcci", 4), 2),
        (("eduktdb", 15), 5),
    ]
)
def testSolution(test_input, expected):
    assert Solution().longestIdealString(*test_input) == expected
