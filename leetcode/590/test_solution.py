import pytest

from solution import Solution, Node

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)]), ), [5, 6, 3, 2, 4, 1]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().postorder(*test_input) == expected
