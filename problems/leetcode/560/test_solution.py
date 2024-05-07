import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 1, 1], 2), 2),
    (([1, 2, 3], 3), 2),
])
def test_solution(test_input, expected):
    sol = Solution()
    assert sol.subarraySum(*test_input) == expected
