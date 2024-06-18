import pytest
from typing import List, Optional

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([2,1,5,6,2,3],), 10),
    (([2,1,6,5,2,3],), 10),
    (([2,4],), 4),
    (([2,0,2],), 2),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.largestRectangleArea(*test_input)
    assert actual == expected
