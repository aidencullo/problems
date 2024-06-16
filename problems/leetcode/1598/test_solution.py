# test_solution.py

import pytest
from solution import Solution

@pytest.mark.parametrize("logs, expected_output", [
    (["d1/", "d2/", "../", "d21/", "./"], 2),
    (["d1/", "d2/", "./", "d3/", "../", "d31/"], 3),
    (["d1/", "../", "../", "../"], 0),
    (["./", "../", "./"], 0),
    (["d1/", "d2/", "d3/", "../", "../", "../"], 0),
    (["d1/", "d2/", "d3/"], 3)
])
def test_minOperations(logs, expected_output):
    solution = Solution()
    assert solution.minOperations(logs) == expected_output
