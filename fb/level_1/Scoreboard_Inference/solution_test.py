from typing import List

import pytest

from solution import getMinProblemCount

test_data_getMinProblemCount: List[tuple[int, List[int], int]] = [
    (6, list(range(1, 7)), 4),
    (4, [4, 3, 3, 4], 3),
    (4, [2, 4, 6, 8], 4),
    (3, [1, 2, 3], 2),
    (2, [1, 11], 6),
    (2, [1, 11], 6),
]

@pytest.mark.parametrize("N, S, expected",
                         test_data_getMinProblemCount)
def test_getMinProblemCount(N: int, S: List[int], expected: int):
    # Assert
    assert getMinProblemCount(N, S) == expected
