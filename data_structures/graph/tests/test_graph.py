import pytest

from src.graph import Graph

@pytest.mark.graph
class TestGraph:

    @pytest.fixture
    def graph(self, ):
        g = Graph()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        return g

    def test_add_vertex(self, graph):
        assert 'A' in graph.vertices
        assert 'B' in graph.vertices
        assert 'C' in graph.vertices

    def test_add_edge(self, graph):
        assert 'B' in graph.vertices['A']
        assert 'C' in graph.vertices['B']

    def test_get_neighbors(self, graph):
        assert graph.get_neighbors('A') == ['B']
        assert graph.get_neighbors('B') == ['C']

    def test_add_edge_invalid_vertex(self, graph):
        with pytest.raises(ValueError):
            graph.add_edge('A', 'D')

    def test_get_neighbors_invalid_vertex(self, graph):
        with pytest.raises(KeyError):
            graph.get_neighbors('D')
