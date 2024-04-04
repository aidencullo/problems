from typing import List

import pytest

from solution import getMinCodeEntryTime

test_data_getMinCodeEntryTime: List[tuple[int, int, List[int], int]] = [
    (3, 3, [1, 2, 3], 2),
    (10, 4, [9, 4, 4, 8], 11),
    (20, 4, [9, 4, 4, 8], 17),
]

@pytest.mark.parametrize("N, M, C, expected",
                         test_data_getMinCodeEntryTime)
def test_getMinCodeEntryTime(N: int, M: int, C: List[int], expected: int):
    # Assert
    assert getMinCodeEntryTime(N, M, C) == expected
