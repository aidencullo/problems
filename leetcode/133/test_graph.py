import pytest

from solution import Solution
from graph import buildGraph, compareGraphIds, compareGraphValues

def testBuildGraph():
    # Act
    edges = [[1,2],[2,3],[3,4],[4,1]]

    # Act
    nodes = buildGraph(edges)

    # Assert
    for node in nodes:
        for neighbor in node.neighbors:
            assert neighbor in nodes


def testCompareGraphValues():
    # Act
    edges = [[1,2],[2,3],[3,4],[4,1]]

    # Act
    nodes = list(buildGraph(edges))
    root = nodes[0]
    nodes2 = list(buildGraph(edges))
    root2 = nodes2[0]

    # Assert
    assert compareGraphValues(root, root)
    assert compareGraphValues(root, root2)
    assert compareGraphIds(root, root)
    assert not compareGraphIds(root, root2)
