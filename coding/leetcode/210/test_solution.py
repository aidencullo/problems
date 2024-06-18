import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((2, [[1,0]]), [0,1]),
    ((4, [[1,0],[2,0],[3,1],[3,2]]), [0,1,2,3]),
    ((1, []), [0]),
    ((2, [[0,1],[1,0]]), []),
])
def test_solution(test_input, expected):
    assert Solution().findOrder(*test_input) == expected
