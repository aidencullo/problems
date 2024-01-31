from typing import List

import pytest

from solution import getArtisticPhotographCount

test_data_getArtisticPhotographCount: List[tuple[int, str, int, int, int]] = [
    (5, "APABA", 1, 2, 1),
    (5, "APABA", 2, 3, 0),
    (8, ".PBAAP.B", 1, 3, 3),
    (1, ".", 1, 3, 0),
    (5, ".....", 1, 1, 0),
    (5, ".....", 1, 3, 0),
    (5, "AAAAA", 1, 3, 0),
    (6, "AAAABP", 1, 3, 0),
    (3, "PAB", 1, 2, 1),
    (4, "PABB", 1, 2, 2),
    (5, "PABBB", 1, 2, 2),
    (5, "PPPAB", 1, 2, 2),
]

@pytest.mark.parametrize("N, C, X, Y, expected",
                         test_data_getArtisticPhotographCount)
def test_getArtisticPhotographCount(N: int, C: str, X: int, Y: int, expected: int):
    # Assert
    assert getArtisticPhotographCount(N, C, X, Y) == expected
