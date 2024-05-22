import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([0,1,0,3,12],), [1,3,12,0,0]),
    (([0],), [0]),
    (([1],), [1]),
    (([0,0,0],), [0,0,0]),
    (([1,2,3],), [1,2,3]),
    (([0,1,0,3,12],), [1,3,12,0,0]),
    (([0,0,1],), [1,0,0]),
])
def test_solution(test_input, expected):
    s = Solution()
    s.moveZeroes(*test_input)
    test_input, = test_input
    assert test_input == expected
