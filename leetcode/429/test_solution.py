import pytest
from solution import Solution, Node


@pytest.mark.parametrize("test_input, expected", [
    ((Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]),), [[1],[3,2,4],[5,6]]),
])
def test_solution(test_input, expected):
    assert Solution().levelOrder(*test_input) == expected
