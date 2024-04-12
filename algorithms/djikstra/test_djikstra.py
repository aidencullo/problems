import pytest
from dijkstra import dijkstra

def test_dijkstra():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }

    assert dijkstra(graph, 'A') == {'A': 0, 'B': 1, 'C': 3, 'D': 4}
