import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1],[2],[3],[]],), True),
        (([[1,3],[3,0,1],[2],[0]],), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().canVisitAllRooms(*test_input) == expected
