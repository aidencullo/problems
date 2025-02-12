import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(3,
                   TreeNode(4,
                            TreeNode(1),
                            TreeNode(2)),
                   TreeNode(5)),
         TreeNode(4,
                  TreeNode(1),
                  TreeNode(2)),
         ),
         True),
    ],
)
def test_single_node(test_input, expected):
    result = Solution().isSubtree(*test_input)
    assert result == expected
