import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3],), [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().subsets(*test_input) == expected
