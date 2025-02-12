import pytest
from solution import TreeNode, Solution

# Define test cases
test_cases = [
    ([1,2,3,4], 4, 3, False),
    ([1,2,3,None,4,None,5], 5, 4, True),
    ([1,2,3,None,4], 2, 3, False),
    # Add more test cases as needed
]

# Define helper function to build a binary tree from list
def build_tree_from_list(nums):
    if not nums:
        return None
    nodes = [None if val is None else TreeNode(val) for val in nums]
    for i, node in enumerate(nodes):
        if node:
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < len(nodes):
                node.left = nodes[left_index]
            if right_index < len(nodes):
                node.right = nodes[right_index]
    return nodes[0]

# Define pytest test function
@pytest.mark.parametrize("tree_values, x, y, expected", test_cases)
def test_isCousins(tree_values, x, y, expected):
    # Build tree from list of values
    root = build_tree_from_list(tree_values)
    # Create solution object
    solution = Solution()
    # Check if nodes are cousins
    assert solution.isCousins(root, x, y) == expected

# Run pytest
if __name__ == "__main__":
    pytest.main()
