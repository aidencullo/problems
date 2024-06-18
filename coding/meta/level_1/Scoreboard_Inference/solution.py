from typing import List

# Write any import statements here

def getMinProblemCount(N: int, S: List[int]) -> int:
  # Write your code here
  last = max(S)
  if hasOdd(S):
    return (last//2) + 1
  else:
    return last // 2

def hasOdd(scores):
  return any(num % 2 != 0 for num in scores)
