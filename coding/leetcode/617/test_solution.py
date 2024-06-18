import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
    ((TreeNode(1,
               TreeNode(3,
                        TreeNode(5)),
               TreeNode(2)),
      TreeNode(2,
               TreeNode(1,
                        right=TreeNode(4)),
               TreeNode(3,
                        right=TreeNode(7)))),
     TreeNode(3,
              TreeNode(4,
                       TreeNode(5),
                       TreeNode(4)),
              TreeNode(5,
                       right=TreeNode(7))))
])
def test_solution(test_input, expected):
    assert compare_trees(Solution().mergeTrees(*test_input), expected)

def compare_trees(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return compare_trees(t1.left, t2.left) and compare_trees(t1.right, t2.right)
