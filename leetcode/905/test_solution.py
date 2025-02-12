import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([3,1,2,4],), [2,4,3,1]),
    (([0],), [0]),
])
def test_solution(test_input, expected):
    assert Solution().sortArrayByParity(*test_input) == expected
