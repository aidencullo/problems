import pytest
from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1, 2, 3, 1], 3), True),
    (([1, 0, 1, 1], 1), True),
    (([1, 2, 3, 1, 2, 3], 2), False),
])
def test_solution(test_input, expected):
    assert Solution().containsNearbyDuplicate(*test_input) == expected
