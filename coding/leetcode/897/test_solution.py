import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(5,
                   TreeNode(3,
                            TreeNode(2,
                                     TreeNode(1),),
                            TreeNode(4)),
                   TreeNode(6,
                            None,
                            TreeNode(8,
                                     TreeNode(7),
                                     TreeNode(9)))), ),
         TreeNode(1,
                  None,
                  TreeNode(2,
                           None,
                           TreeNode(3,
                                    None,
                                    TreeNode(4,
                                             None,
                                             TreeNode(5,
                                                      None,
                                                      TreeNode(6,
                                                               None,
                                                               TreeNode(7,
                                                                        None,
                                                                        TreeNode(8,
                                                                                 None,
                                                                                 TreeNode(9)))))))))),
    ],
)
def test_solution(test_input, expected):
    assert compare_trees(Solution().increasingBST(*test_input), expected)


def compare_trees(t1, t2):
    if not t1 and not t2:
        return True
    if not t1 or not t2:
        return False
    if t1.val != t2.val:
        return False
    return compare_trees(t1.left, t2.left) and compare_trees(t1.right, t2.right)
    
