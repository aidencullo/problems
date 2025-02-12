import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1,2,1],), [2,-1,2]),
    (([1,2,3,4,3],), [2,3,4,-1,4]),
])
def test_solution(test_input, expected):
    assert Solution().nextGreaterElements(*test_input) == expected
