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


@pytest.mark.nodegraph
class TestNodegraph:

    @pytest.fixture
    def adjacency_list(self):
        return {
            1: [2,],
            2: [3,],
            3: [1,],
        }

    @pytest.fixture
    def node_graph(self, adjacency_list):
        return NodeGraph(adjacency_list)

    def test_create_from_dict(self, adjacency_list):
        ng = NodeGraph(adjacency_list)
        assert 1 in ng._vertices
        assert 2 in ng._vertices
        assert 3 in ng._vertices
    
    def test_get_root(self, node_graph):
        assert node_graph.get_root().val == 1
