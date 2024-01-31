from typing import List

import pytest

from solution import getArtisticPhotographCount

test_data_getArtisticPhotographCount: List[tuple[int, str, int, int, int]] = [
    (5, "APABA", 1, 2, 1),
    (5, "APABA", 2, 3, 0),
    (8, ".PBAAP.B", 1, 3, 3),
]

@pytest.mark.parametrize("N, C, X, Y, expected",
                         test_data_getArtisticPhotographCount)
def test_getArtisticPhotographCount(N: int, C: str, X: int, Y: int, expected: int):
    # Assert
    assert getArtisticPhotographCount(N, C, X, Y) == expected
