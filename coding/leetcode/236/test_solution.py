from solution import TreeNode

import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [



        # (
        #     (
        #         TreeNode(6,
        #                  TreeNode(1),
        #                  TreeNode(5)
        #                  ),
        #         TreeNode(5),
        #         TreeNode(1),
        #     ),
        #     TreeNode(6),
        # ),




        # (
        #     (
        #         TreeNode(3,
        #                  TreeNode(6,
        #                           TreeNode(1),
        #                           TreeNode(5)
        #                           )
        #                  ),
        #         TreeNode(5),
        #         TreeNode(1),
        #     ),
        #     TreeNode(6),
        # ),



        # (
        #     (
        #         TreeNode(3,
        #                  TreeNode(5,
        #                           TreeNode(6),
        #                           TreeNode(2,
        #                                    TreeNode(7),
        #                                    TreeNode(4))),
        #                  TreeNode(1,
        #                           TreeNode(0),
        #                           TreeNode(8))),
        #         TreeNode(5),
        #         TreeNode(1),
        #     ),
        #     TreeNode(3),            
        # ),









        (
            (
                TreeNode(3,
                         TreeNode(5,
                                  TreeNode(6),
                                  TreeNode(2,
                                           TreeNode(7),
                                           TreeNode(4))),
                         TreeNode(1,
                                  TreeNode(0),
                                  TreeNode(8))),
                TreeNode(5),
                TreeNode(4),
            ),
            TreeNode(5),            
        ),




    ]

)
def testSolution(test_input, expected):
    t, _, _ = test_input
    l = t.left
    r = t.left.right.right
    assert Solution().lowestCommonAncestor(t, l, r) == l
