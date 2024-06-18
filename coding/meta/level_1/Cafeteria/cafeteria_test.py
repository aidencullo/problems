from typing import List

import pytest

from cafeteria import getMaxAdditionalDinersCount, getMaxDiners

test_data_getMaxDiners: List[tuple[int, int, int, int]] = [
    (1, 3, 1, 2),
    (1, 10, 1, 5),
    (1, 100, 1, 50),
    (91, 100, 1, 5),
    (5, 5, 1, 1),
    (5, 6, 1, 1),
    (5, 6, 2, 1),
    (5, 6, 100, 1),
    (1, 10, 100, 1),
    (1, 10, 2, 4),
    (4, 3, 2, 0),
    (100, 50, 2, 0),
    (100, 50, 1, 0),
    (100, 50, 100, 0),
]

test_data_getMaxAdditionalDinersCount: List[tuple[int, int, int,
                                                  List[int], int]] = [
    (1, 1, 0, [], 1),
    (1, 2, 0, [], 1),
    (1, 10, 0, [], 1),
    (1, 100, 0, [], 1),
    (1, 10, 1, [1], 0),
    (5, 1, 0, [], 3),
    (5, 2, 0, [], 2),
    (5, 10, 0, [], 1),
    (5, 100, 0, [], 1),
    (5, 10, 1, [1], 0),
    (10, 1, 1, [1], 4),
    (10, 1, 1, [10], 4),
    (10, 2, 1, [10], 3),
    (10, 1, 3, [1, 3, 5], 2),
    (10, 1, 5, [1, 3, 5, 7, 9], 0),
]

@pytest.mark.parametrize("start, end, K, expected", test_data_getMaxDiners)
def test_getMaxDiners(start: int, end: int, K: int, expected: int):
    # Assert
    assert getMaxDiners(start, end, K) == expected


@pytest.mark.parametrize("N, K, M, S, expected",
                         test_data_getMaxAdditionalDinersCount)
def test_getMaxAdditionalDinersCount(N: int, K: int, M: int, S:
                                     list[int], expected: int):
    # Assert
    assert getMaxAdditionalDinersCount(N, K, M, S) == expected
