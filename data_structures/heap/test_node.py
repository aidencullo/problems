import pytest

from node import Node

@pytest.mark.node
class TestNode:

    def test_single_node_value(self):
        assert Node(1).val == 1
        assert Node().val == 0


    def test_single_node_no_children(self):
        assert not Node().left
        assert not Node().right


    def test_single_node_two_children(self):
        assert Node(1, Node()).left
        assert Node(1, Node(), Node()).right
