import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((TreeNode(5, TreeNode(2), TreeNode(-3)),), [4, 2, -3]),
        ((TreeNode(5, TreeNode(2), TreeNode(-5)),), [2]),
    ],
)
def test_solution(test_input, expected):
    assert compare(Solution().findFrequentTreeSum(*test_input), expected)

def compare(a, b):
    return sorted(a) == sorted(b)
