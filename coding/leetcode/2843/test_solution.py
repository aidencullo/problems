# test_solution.py

import pytest
from solution import Solution

@pytest.mark.parametrize("low, high, expected_output", [
    (1, 100, 9),
    (1200, 1230, 4),
    (10, 30, 2),
    (100, 1782, 44),
])
def test_countSymmetricIntegers(low, high, expected_output):
    solution = Solution()
    assert solution.countSymmetricIntegers(low, high) == expected_output
