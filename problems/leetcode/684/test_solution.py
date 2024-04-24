import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ([[1,2],[1,3],[2,3]], [2,3]),
    ([[1,2],[2,3],[3,4],[1,4],[1,5]], [1,4]),
])
def test_solution(test_input, expected):
    assert Solution().findRedundantConnection(test_input) == expected
