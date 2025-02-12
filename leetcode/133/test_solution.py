import pytest

from solution import Solution
from graph import buildGraph, compareGraphByValue, compareGraphById

@pytest.fixture(params=[
    ([[1,2],[2,3],[3,4],[4,1],], 4),
    ([[1,2],[2,3],[3,4],], 4),
    ([[1,2],], 2),
])
def test_input(request):
    g = buildGraph(*request.param)
    return g

def testSolution(test_input):
    actual = Solution().cloneGraph(test_input)
    assert compareGraphByValue(actual, test_input)
    assert not compareGraphById(actual, test_input)

   
@pytest.fixture(params=[
    ([[],], 0),
])
def testSolutionNull(test_input):
    actual = Solution().cloneGraph(test_input)
    assert compareGraphByValue(actual, test_input)
    assert compareGraphById(actual, test_input)
