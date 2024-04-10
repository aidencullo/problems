import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([0,1,0,2,1,0,1,3,2,1,2,1],), 6),
    (([4,2,0,3,2,5],), 9),
    (([2,0,2],), 2),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.trap(*test_input) == expected
