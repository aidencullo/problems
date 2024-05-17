import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(1, None, TreeNode(2, TreeNode(3), None)), ), [3, 2, 1]),
        ((TreeNode(1), ), [1]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().postorderTraversal(*test_input) == expected
