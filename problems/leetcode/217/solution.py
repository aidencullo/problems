## Solution 1
# from typing import Optional, List, Tuple
# from collections import Counter

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return any(c > 1 for c in Counter(nums).values())
 
## Solution 2
# from typing import Optional, List, Tuple
# from collections import Counter

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         return len(set(nums)) != len(nums)

 
## Solution 3
# from typing import Optional, List, Tuple
# from collections import Counter

# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#         return False







## Solution 4
from typing import Optional, List, Tuple
from collections import Counter

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(dict.fromkeys(nums)) != len(nums)
