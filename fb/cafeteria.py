from typing import List
from math import ceil
from icecream import ic

# def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
#   # Write your code here
#   S = sorted(S)
#   diners = 0
#   i = 1
#   start = i
#   while i < N + 1:
#     if i in S:
#       end = i - (K+1)
#       diners += calculateDiners(start, end, K)
#       i += K+1
#       start = i
#     elif i == N:
#       end = i
#       diners += calculateDiners(start, end, K)
#       i += 1
#     else:
#       i += 1
#   return diners

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S = list(reversed(sorted(S)))
  diners = 0
  start = 1
  while S:
    diner = S.pop()
    ic(getMaxDiners(start, diner - K, K))
    diners += getMaxDiners(start, diner - K, K)
    start = diner + K + 1
  diners += getMaxDiners(start, N, K)
  return diners

def getMaxDiners(start, end, K):
  seats = end - start + 1
  seats = max(0, seats)
  return ceil(seats/(K+1))
