from solution import Solution, TreeNode


import pytest

def test_averageOfSubtree():
    # Helper function to build tree from list
    def build_tree(nodes, index=0):
        if index < len(nodes) and nodes[index] is not None:
            node = TreeNode(nodes[index])
            node.left = build_tree(nodes, 2 * index + 1)
            node.right = build_tree(nodes, 2 * index + 2)
            return node
        return None

    # Test case 1
    nodes1 = [4, 8, 5, 0, 1, None, 6]
    root1 = build_tree(nodes1)
    assert Solution().averageOfSubtree(root1) == 5

    # Test case 2
    nodes2 = [1]
    root2 = build_tree(nodes2)
    assert Solution().averageOfSubtree(root2) == 1

    # Test case 3
    nodes3 = [0, 0, 0]
    root3 = build_tree(nodes3)
    assert Solution().averageOfSubtree(root3) == 3

    # Test case 4
    nodes4 = [1, 2, 3, 4, 5, 6, 7]
    root4 = build_tree(nodes4)
    assert Solution().averageOfSubtree(root4) == 7

    # Test case 5: Tree with negative values
    nodes5 = [-1, -2, -3, -4, -5]
    root5 = build_tree(nodes5)
    assert Solution().averageOfSubtree(root5) == 3

    # Test case 6: Tree with only one subtree
    nodes6 = [1, 2, None, 3, 4]
    root6 = build_tree(nodes6)
    assert Solution().averageOfSubtree(root6) == 2

# Running the tests
pytest.main()
