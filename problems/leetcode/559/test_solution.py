import pytest

from solution import Solution, Node

@pytest.mark.parametrize("test_input, expected", [
    ((Node(3, [Node(9), Node(20, [Node(15), Node(7)])]),), 3),
])
def test_solution(test_input, expected):
    assert Solution().maxDepth(*test_input) == expected
