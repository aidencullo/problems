import pytest

from solution import Solution
from graph import buildGraph, compareGraphByValue, compareGraphById


def testBuildGraph():
    test_input = [[1,2],[2,3],[3,4],[4,1],]
    node = buildGraph(test_input, 4)
    assert node.val == 1
    for neighbor in node.neighbors:
        assert neighbor.val in [2,4]
        assert len(neighbor.neighbors) == 2


def testBuildGraph2():
    test_input = [[1,2],[2,3],[3,4],]
    node = buildGraph(test_input, 4)
    assert node.val == 1
    assert len(node.neighbors) == 1
    assert node.neighbors[0].val == 2
    assert len(node.neighbors[0].neighbors) == 2
    assert node.neighbors[0].neighbors[1].val == 3
    assert node.neighbors[0].neighbors[1].neighbors[1].val == 4


def testCompareGraphByValueEqual():
    test_input = [[1,2],[2,3],[3,4],]
    node = buildGraph(test_input, 4)
    assert compareGraphByValue(node, node)


def testCompareGraphByValueNotEqual():
    test_input = [[1,2],[2,3],[3,4],]
    node = buildGraph(test_input, 4)
    test_input2 = [[1,2],[2,3],]
    node2 = buildGraph(test_input2, 3)
    assert not compareGraphByValue(node, node2)


def testCompareGraphByValueEqual2():
    test_input = [[1,2],]
    node = buildGraph(test_input, 2)
    test_input2 = [[1,2],[2,1],]
    node2 = buildGraph(test_input2, 2)
    assert not compareGraphByValue(node, node2)


def testCompareGraphByIdEqual():
    test_input = [[1,2],[2,3],[3,4],]
    node = buildGraph(test_input, 4)
    assert compareGraphById(node, node)

    
def testCompareGraphByIdNotEqual():
    test_input = [[1,2],[2,3],[3,4],]
    node = buildGraph(test_input, 4)
    node2 = buildGraph(test_input, 4)
    assert not compareGraphById(node, node2)

def testbuildGraphEmpty():
    test_input = []
    node = buildGraph(test_input, 0)
    assert not node
