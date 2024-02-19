import pytest

from solution import Solution
from util import compareTree, makeTree

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
        ([2, 1, 3], [2, 3, 1]),
    ],
)
def test_single_node(test_input, expected):
    # Arrange
    input_tree = makeTree(test_input)
    expected_tree = makeTree(expected)

    # Act
    result_tree = Solution().invertTree(input_tree)

    # Assert    
    assert compareTree(result_tree, expected_tree)


def test_makeTree():
    # Arrange
    l = [4,2,7,1,3,6,9]

    # Act
    t = makeTree(l)

    # Assert
    assert t.val == 4
    assert t.right.right.val == 9


def test_makeTree_1():
    # Arrange
    l = [1,0,7,1,3,5,9]
    # Act
    t = makeTree(l)

    # Assert
    assert t.val == 1
    assert t.left.val == 0
    assert t.right.val == 7
    assert t.right.left.val == 5

def test_compareTree():
    # Arrange
    l = [1,0,7,1,3,5,9]
    # Act
    t = makeTree(l)
    
    # Assert
    assert compareTree(t, t)
