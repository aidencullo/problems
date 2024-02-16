from collections import Counter
import math
    
## O(n^2) time O(n^2) space
# def distinct_words(password):        
#         n = len(password)
#         total = {password}
#         for i in range(n):
#             for j in range(i + 2, n + 1):
#                 new_password = password[:i] + password[i:j][::-1] + password[j:]
#                 total.add(new_password)
#         return len(total)

## O(1) time O(n) space
def distinct_words(password):
        total = sum(range(len(password)))
        frequencies = Counter(password).values()
        multiples = sum(sum(range(freq)) for freq in frequencies)
        return total + 1 - multiples
