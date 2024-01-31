from typing import List

import pytest

from solution import getMaximumEatenDishCount

# Sample test case #2
# N = 6
# D = [1, 2, 3, 3, 2, 1]
# K = 2
# Expected Return Value = 4
# Sample test case #3
# N = 7
# D = [1, 2, 1, 2, 1, 2, 1]
# K = 2
# Expected Return Value = 2

test_data_getMaximumEatenDishCount: List[tuple[int, List[int], int, int]] = [
    (6, [1, 2, 3, 3, 2, 1], 1, 5),
    (6, [1, 2, 3, 3, 2, 1], 2, 4),
    (7, [1, 2, 1, 2, 1, 2, 1], 2, 2),
]

@pytest.mark.parametrize("N, D, K, expected",
                         test_data_getMaximumEatenDishCount)
def test_getMaximumEatenDishCount(N: int, D: str, K: int, expected: int):
    # Assert
    assert getMaximumEatenDishCount(N, D, K) == expected
