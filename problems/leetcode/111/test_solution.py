import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7))),), 2),
    ((TreeNode(2, None, TreeNode(3, None, TreeNode(4, None, TreeNode(5, None, TreeNode(6))))),), 5),
    ((None,), 0),
    ((TreeNode(1, TreeNode(2)),), 2),
    ((TreeNode(1, None, TreeNode(2)),), 2),
    ((TreeNode(1, TreeNode(2), TreeNode(3)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5))), TreeNode(6)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5))), TreeNode(6)), TreeNode(7)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5), TreeNode(6))), TreeNode(7)), TreeNode(8)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6))), TreeNode(7)), TreeNode(8)), TreeNode(9)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7)))), TreeNode(8)), TreeNode(9)), TreeNode(10)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7, TreeNode(8)))), TreeNode(9)), TreeNode(10)), TreeNode(11)), TreeNode(12)),), 2),
    ((TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4, TreeNode(5, TreeNode(6, TreeNode(7, TreeNode(8, TreeNode(9)))), TreeNode(10)), TreeNode(11)), TreeNode(12)), TreeNode(13)), TreeNode(14)),), 2),
])
def test_solution(test_input, expected):
    assert Solution().minDepth(*test_input) == expected
