import pytest

from solution import Solution
from graph import buildGraph, compareGraphsId, compareGraphsValue

@pytest.mark.skip
@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([[2,4],[1,3],[2,4],[1,3]], None),
    ],
)
def testSolution(test_input, expected):
    # Arrange
    s = Solution()

    # Act
    g = buildGraph(test_input)
    actual = s.cloneGraph(g)

    # Assert
    assert not compareGraphsId(actual, g)
    assert compareGraphsValue(actual, g)
