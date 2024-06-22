import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(1, None, TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, None)))),), TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4))),
    ],
)
def test_solution(test_input, expected):
    assert Solution().balanceBST(*test_input) == expected
