from solution import TreeNode

import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [


        (
            (
                TreeNode(6,
                         TreeNode(2,
                                  TreeNode(0),
                                  TreeNode(4,
                                           TreeNode(3),
                                           TreeNode(5)
                                           )
                                  ),
                         TreeNode(8,
                                  TreeNode(7),
                                  TreeNode(9)
                                  )
                         ),
                TreeNode(2),
                TreeNode(8),
            ),
            TreeNode(6),
        ),
        
# [6,2,8,0,4,7,9,null,null,3,5]


    ]

)
def testSolution(test_input, expected):
    assert Solution().lowestCommonAncestor(*test_input).val == expected.val
