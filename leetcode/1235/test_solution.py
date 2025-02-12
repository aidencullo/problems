import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 3, 3], [3, 4, 5, 6], [50, 10, 40, 70],), 120),
    (([1, 2, 3, 4, 6], [3, 5, 10, 6, 9], [20, 20, 100, 70, 60],), 150),
    (([1, 1, 1], [2, 3, 4], [5, 6, 4],), 6),
    (([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60],), 150),
    (([4,3,1,2,4,8,3,3,3,9], [5,6,3,5,9,9,8,5,7,10], [9,9,5,12,10,11,10,4,14,7],), 37),
])
def test_solution(test_input, expected):
    sol = Solution()
    actual = sol.jobScheduling(*test_input)
    assert actual == expected
