# # Solution 1
# """
# slow according to leet
# """
# # O(d) time and space where d is the combined number of digits
# class Solution:
#     def addBinary(self, a: str, b: str) -> str:
#         return bin(int(a, base=2) + int(b, base=2)).split('b')[1]






import itertools

# Solution 2
"""
slighly faster, but so messy
"""
# O(d) time and space where d is the combined number of digits
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m = max(len(a), len(b))
        a = a.zfill(m)
        b = b.zfill(m)
        carry = 0
        result = ''
        for i, j in zip(a[::-1], b[::-1]):
            current_digit = get_current_digit(i, j, carry)
            carry = get_next_digit(i, j, carry)
            result = current_digit + result
        if int(carry):                
            result = '1' + result
        return result

def get_current_digit(i, j, k):
    i = int(i)
    j = int(j)
    k = int(k)
    return str((i + j + k) % 2)
    
def get_next_digit(i, j, k):
    i = int(i)
    j = int(j)
    k = int(k)
    return str(int((i + j + k) // 2))
