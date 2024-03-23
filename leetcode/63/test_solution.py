import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[0,0,0],[0,1,0],[0,0,0]],), 2),
        (([[0,0,0],[0,0,0],[0,0,0]],), 6),
        (([[0,0,0],[0,0,0]],), 3),
        (([[0,1],[0,0]],), 1),
        (([[0,1]],), 0),
        (([[1,1]],), 0),
        (([[0,1],[0,0]],), 1),
        (([[0,1]],), 0),
        (([[1,1]],), 0),
    ]
)
def testSolution(test_input, expected):
    assert Solution().uniquePathsWithObstacles(*test_input) == expected
