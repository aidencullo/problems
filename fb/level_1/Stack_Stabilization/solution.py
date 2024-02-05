from typing import List
import math
# Write any import statements here

def getMinimumDeflatedDiscCount(N: int, R: List[int]) -> int:
  # Write your code here
  min_disc = math.inf
  deflated = 0
  for disc in R[::-1]:
    if disc < min_disc:
      min_disc = disc
    elif min_disc > 1:
      deflated += 1
      min_disc -= 1
    else:
      return -1
  return deflated
