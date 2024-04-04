import pytest
from kthSmallest import Solution
from kthSmallest import TreeNode

# Define test cases
@pytest.mark.parametrize("tree, k, expected", [
    (TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4)), 1, 1),
    (TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 3, 3),
    (TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 4, 4),
    (TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6)), 5, 5),
    (TreeNode(31, TreeNode(30, TreeNode(3, TreeNode(0)))), 1, 0),
    # Add more test cases as needed
])
def test_kth_smallest(tree, k, expected):
    sol = Solution()
    assert sol.kthSmallest(tree, k) == expected
