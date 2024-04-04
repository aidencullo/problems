from typing import List

import pytest

from solution import getMinimumDeflatedDiscCount

test_data_getMinimumDeflatedDiscCount: List[tuple[int, List[int], int]] = [
    (5, [2, 5, 3, 6, 5], 3),
    (3, [100, 100, 100], 2),
    (4, [6, 5, 4, 3], -1),
]

@pytest.mark.parametrize("N, R, expected",
                         test_data_getMinimumDeflatedDiscCount)
def test_getMinimumDeflatedDiscCount(N: int, R: List[int], expected: int):
    # Assert
    assert getMinimumDeflatedDiscCount(N, R) == expected
