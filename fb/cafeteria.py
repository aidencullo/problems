from typing import List
from math import ceil
# Write any import statements here
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  # Write your code here
  S = sorted(S)
  diners = 0
  i = 1
  start = i
  while i < N + 1:
    if i in S:
      end = i - (K+1)
      diners += calculateDiners(start, end, K)
      i += K+1
      start = i
    elif i == N:
      end = i
      diners += calculateDiners(start, end, K)
      i += 1
    else:
      i += 1
  return diners

def calculateDiners(start, end, K):
  seats = end - start + 1
  return ceil(seats/(K+1))

from dataclasses import dataclass, astuple

@dataclass(frozen=True)
class TestCase:
  N: int
  K: int
  M: int
  S: [int]
  expected: int
  test: int

  def __iter__(self):
    return (i for i in astuple(self))

def test(test_case):
  N, K, M, S, expected, test = test_case
  result = getMaxAdditionalDinersCount(N, K, M, S)
  print()
  print(f'{test=}')
  if result == expected:
    print(f'passed')
  else:
    print(f'passed')
    print(f'{test_case=}')
    print(f'{expected=}')
    print(f'{result=}')

  
N = 10
K = 1
M = 2
S = [2, 6]
expected = 3

test(TestCase(N, K, M, S, expected, 1))

N = 15
K = 2
M = 3
S = [11, 6, 14]
expected = 1

test(TestCase(N, K, M, S, expected, 2))

N = 3
K = 3
M = 0
S = []
expected = 1

test(TestCase(N, K, M, S, expected, 3))


N = 5
K = 2
M = 1
S = [2]
expected = 1

test(TestCase(N, K, M, S, expected, 4))


N = 100
K = 20
M = 2
S = [2,10]
expected = 4

test(TestCase(N, K, M, S, expected, 4))
