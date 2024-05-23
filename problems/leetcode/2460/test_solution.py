import pytest
from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (([1,2,2,1,1,0],), [1,4,0,2,0,0]),
])
def test_solution(test_input, expected):
    s = Solution()
    result = s.applyOperations(*test_input)
    assert result == expected
