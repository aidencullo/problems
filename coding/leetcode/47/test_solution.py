import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 1, 2],), [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        (([1, 2, 3],), [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().permuteUnique(*test_input) == expected
