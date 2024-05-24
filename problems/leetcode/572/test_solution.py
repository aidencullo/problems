import pytest

from solution import Solution, TreeNode

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
    ],
)
def test_single_node(test_input, expected):
    result = Solution().isSubtree(*test_input)
    assert result == expected
