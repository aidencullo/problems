import pytest

from solution import Solution
from graph import buildGraph, compareGraphsId, compareGraphsValue

def testBuildGraph():
    # Act
    edges = [[2,4],[1,3],[2,4],[1,3]]

    # Act
    root = buildGraph(edges)

    # Assert
    assert root.val == 2
    for neighbor in root.neighbors:
        assert neighbor.val in [4]
