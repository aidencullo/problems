import pytest

from solution import Solution, TreeNode
from util import makeTree, inOrder, preOrder, postOrder, countNodes, isPerfect, height

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([6,2,8,0,4,7,9,None,None,3,5], 2, 8), 6),
        (([6,2,8,0,4,7,9,None,None,3,5], 2, 4), 2),
        (([2, 1], 2, 1), 2),
    ],
)
def testSolution(test_input, expected):
    # Act
    lst, p, q = test_input
    tree: TreeNode = makeTree(lst)
    expected: TreeNode = TreeNode(expected)
    result = Solution().lowestCommonAncestor(tree, TreeNode(p), TreeNode(q))

    # Assert    
    assert result == expected

def testInOrder():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = [1, 2, 3, 5, 1, 2, 3]

    # Act
    result = inOrder(otherTree)

    # Assert    
    assert result == expected


def testPreOrder():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = [5, 2, 2, 1, 3, 1, 3]

    # Act
    result = preOrder(otherTree)

    # Assert    
    assert result == expected


def testPostOrder():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = [1, 3, 2, 1, 3, 2, 5]

    # Act
    result = postOrder(otherTree)

    # Assert    
    assert result == expected

    
def testCountNodes():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = 7

    # Act
    result = countNodes(otherTree)

    # Assert    
    assert result == expected

def testCountNodes2():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = 5

    # Act
    result = countNodes(otherTree)

    # Assert    
    assert result == expected


def testIsPerfectSuccess():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    otherTree.right = tree
    expected = 7

    # Act
    result = countNodes(otherTree)

    # Assert    
    assert isPerfect(otherTree)


def testIsPerfectFail():
    # Arrange
    tree: TreeNode = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(3)
    otherTree: TreeNode = TreeNode(5)
    otherTree.left = tree
    expected = 7

    # Act
    result = countNodes(otherTree)

    # Assert    
    assert not isPerfect(otherTree)


def testMakeTree():
    # Arrange
    lst = [6,2,8,0,4,7,9,None,None,3,5]

    # Act
    result: TreeNode = makeTree(lst)

    # Assert    
    assert result.val == 6
    assert result.right.val == 8
    assert result.left.val == 2
    assert result.left.right.val == 4


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(),), 1),
        ((TreeNode(left=TreeNode(), right=TreeNode()),), 2),
        ((TreeNode(left=TreeNode(left=TreeNode()), right=TreeNode()),), 3),
        ((TreeNode(left=TreeNode()),), 2),
    ],
)
def testHeight(test_input, expected):
    # Assert    
    assert height(*test_input) == expected
