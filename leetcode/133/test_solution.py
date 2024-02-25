import pytest

from solution import Solution
from graph import buildGraph, compareGraphIds, compareGraphValues

@pytest.fixture(params=[
    [[1,2],[2,3],[3,4],[4,1],],
    [[1,2],[2,3],[3,4],],
    [[1,2],],
])
def test_input(request):
    g = buildGraph(request.param)
    return g[0] if g else None

def testSolution(test_input):
    actual = Solution().cloneGraph(test_input)
    assert not compareGraphIds(actual, test_input)
    assert compareGraphValues(actual, test_input)
