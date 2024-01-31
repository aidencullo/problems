from typing import List
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten: List[int] = []
  for index, dish in enumerate(D):
    if dish not in eaten[:K]:
      eaten.insert(0, dish)
  return len(eaten)
