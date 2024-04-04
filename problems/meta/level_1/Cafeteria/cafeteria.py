from typing import List
from math import ceil


def getMaxAdditionalDinersCount(N: int,
                                K: int,
                                _: int,
                                S: List[int]) -> int:
    # Write your code here
    S = list(reversed(sorted(S)))
    diners = 0
    start = 1
    while S:
        diner = S.pop()
        diners += getMaxDiners(start, diner - (K + 1), K)
        start = diner + K + 1
    diners += getMaxDiners(start, N, K)
    return diners


def getMaxDiners(start, end, K):
    seats = end - start + 1
    seats = max(0, seats)
    return ceil(seats/(K+1))
