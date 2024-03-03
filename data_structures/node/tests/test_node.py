import pytest

from src.node import Node

@pytest.mark.node
class TestNode:

    @pytest.fixture
    def node(self, ):
        n = Node(1, Node(2), Node(3))
        return n

    def test_vals(self, node):
        assert node.val == 1
        assert node.left.val == 2
        assert node.right.val == 3
