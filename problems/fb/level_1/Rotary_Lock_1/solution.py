from typing import List
# Write any import statements here

def getMinCodeEntryTime(N: int, M: int, C: List[int]) -> int:
  # Write your code here
  current = 1
  total = 0
  for num in C:
    total += timeBetween(current, num, N)
    current = num
  return total

def timeBetween(current, next, N):
  return min((next-current) % N, (current-next) % N)
