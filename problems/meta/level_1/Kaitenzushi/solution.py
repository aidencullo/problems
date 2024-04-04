from typing import List
from collections import deque
# Write any import statements here

def getMaximumEatenDishCount(N: int, D: List[int], K: int) -> int:
  # Write your code here
  eaten = 0
  recent = deque()
  search_set = set()
  for index, dish in enumerate(D):
    if dish not in search_set:
      eaten += 1
      recent.append(dish)
      search_set.add(dish)
      if len(recent) > K:
        search_set.remove(recent.popleft())
  return eaten

