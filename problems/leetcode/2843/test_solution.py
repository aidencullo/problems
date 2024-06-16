# test_solution.py

import pytest
from solution import Solution

@pytest.mark.parametrize("low, high, expected_output", [
    (1, 100, 9),
    # (1200, 1230, 4),
    # (10, 30, 1),
    # (100, 200, 19),
    # (1000, 1100, 19),
    # (777, 888, 6),
])
def test_countSymmetricIntegers(low, high, expected_output):
    solution = Solution()
    assert solution.countSymmetricIntegers(low, high) == expected_output
