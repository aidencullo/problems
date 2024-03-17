import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[2,1,1],[1,1,0],[0,1,1]],), 4),
        (([[2,1,1],[0,1,1],[1,0,1]],), -1),
        (([[0]],), 0),
    ]

)
def testSolution(test_input, expected):
    assert Solution().orangesRotting(*test_input) == expected
