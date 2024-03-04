import pytest

from src.graph import Graph, NodeGraph

@pytest.mark.graph
class TestGraph:

    @pytest.fixture(scope="module", params=[Graph, NodeGraph])
    def graph(self, request):
        g = request.param()
        g.add_vertex('A')
        g.add_vertex('B')
        g.add_vertex('C')
        g.add_edge('A', 'B')
        g.add_edge('B', 'C')
        return g

    def test_add_vertex(self, graph):
        assert 'A' in graph._vertices
        assert 'B' in graph._vertices
        assert 'C' in graph._vertices

    def test_add_edge(self, graph):
        assert 'B' in graph.get_neighbors('A')
        assert 'C' in graph.get_neighbors('B')

    def test_get_neighbors(self, graph):
        assert graph.get_neighbors('A') == ['B']
        assert graph.get_neighbors('B') == ['C']

    def test_add_edge_invalid_vertex(self, graph):
        with pytest.raises(ValueError):
            graph.add_edge('A', 'D')

    def test_get_neighbors_invalid_vertex(self, graph):
        with pytest.raises(KeyError):
            graph.get_neighbors('D')
