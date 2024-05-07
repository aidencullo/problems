from dijkstra import dijkstra


def test_shortest_path():
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    assert dijkstra(graph, 'A', 'D') == ('ABCD', 4)


def test_no_path():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {}
    }
    assert dijkstra(graph, 'A', 'C') == ('', float('inf'))


def test_no_path_from_start():
    graph = {
        'A': {},
        'B': {'A': 1},
        'C': {'B': 2}
    }
    assert dijkstra(graph, 'A', 'C') == ('', float('inf'))

def test_connected_graph():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1}
    }
    assert dijkstra(graph, 'A', 'B') == ('AB', 1)


def test_disconnected_graph():
    graph = {
        'A': {'B': 1},
        'B': {'A': 1},
        'C': {'D': 1},
        'D': {'C': 1}
    }
    assert dijkstra(graph, 'A', 'C') == ('', float('inf'))
    assert dijkstra(graph, 'A', 'D') == ('', float('inf'))
    assert dijkstra(graph, 'B', 'C') == ('', float('inf'))
    assert dijkstra(graph, 'B', 'D') == ('', float('inf'))
    assert dijkstra(graph, 'C', 'A') == ('', float('inf'))
    assert dijkstra(graph, 'C', 'B') == ('', float('inf'))
    assert dijkstra(graph, 'D', 'A') == ('', float('inf'))
    assert dijkstra(graph, 'D', 'B') == ('', float('inf'))

def test_free_code_camp():
# https://www.freecodecamp.org/news/dijkstras-shortest-path-algorithm-visual-introduction/

    graph = {
        'A': {'B': 6, 'D': 1},
        'B': {'A': 6, 'D': 2, 'E': 2, 'C': 5},
        'C': {'B': 5, 'E': 5},
        'D': {'A': 1, 'B': 2, 'E': 1},
        'E': {'B': 2, 'D': 1, 'C': 5}
    }

    assert dijkstra(graph, 'A', 'C') == ('ADEC', 7)
