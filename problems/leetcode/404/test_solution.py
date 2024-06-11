import pytest

# Import the TreeNode class and Solution class from the solution file
from solution import TreeNode, Solution

# Define test cases using pytest
class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_example1(self, solution):
        root = TreeNode(3)
        root.left = TreeNode(9)
        root.right = TreeNode(20)
        root.right.left = TreeNode(15)
        root.right.right = TreeNode(7)
        assert solution.sumOfLeftLeaves(root) == 24

    def test_example2(self, solution):
        root = TreeNode(1)
        assert solution.sumOfLeftLeaves(root) == 0

    def test_empty_tree(self, solution):
        assert solution.sumOfLeftLeaves(None) == 0

    def test_single_node(self, solution):
        root = TreeNode(5)
        assert solution.sumOfLeftLeaves(root) == 0

