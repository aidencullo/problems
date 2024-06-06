import pytest

from solution import Solution, TreeNode


@pytest.mark.parametrize("test_input, expected", [
])
def test_solution(test_input, expected):
    assert Solution().getTargetCopy(*test_input) == expected
