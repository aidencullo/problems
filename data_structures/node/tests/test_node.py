import pytest

from src.node import Node

@pytest.mark.node
class TestNode:

    @pytest.fixture
    def node(self, ):
        n = Node(1)
        l = Node(2)
        r = Node(3)
        n.add_edge(l)
        n.add_edge(r)
        return n

    def test_node_with_two_edges(self, node):
        assert node.val == 1
        for edge in node.edges:
            assert edge.val in [2, 3]
