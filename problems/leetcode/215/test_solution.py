import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([3,2,1,5,6,4], 2), 5),
    (([3,2,3,1,2,4,5,5,6], 4), 4),
    (([1], 1), 1),
    (([3,2,1,5,6,4], 2), 5),
])
def test_solution(test_input, expected):
    sol = Solution().findKthLargest(*test_input)
