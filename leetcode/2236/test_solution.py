import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([4,2,5,7],), [4,5,2,7]),
    (([2,3],), [2,3]),
    (([3,4],), [4,3]),
])
def test_solution(test_input, expected):
    assert Solution().sortArrayByParityII(*test_input) == expected
