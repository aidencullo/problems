
# # O(n^3) solution
# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         n = len(s)
#         palindromes = 0

#         for i in range(n, 0, -1):
#             for j in range(i):
#                 if is_palindrome(s[j:i]):
#                     palindromes += 1
#         return palindromes

# def is_palindrome(s):
#     n = len(s)
#     for i in range(n):
#         if s[i] != s[n - i - 1]:
#             return False
#     return True


# s = Solution()

# input_1 = "abc"
# expected_1 = 3
# assert s.countSubstrings(input_1) == expected_1
# input_2 = "aaa"
# expected_2 = 6
# assert s.countSubstrings(input_2) == expected_2



class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindromes = 0

        for i in range(n):
            palindromes += count_palindromes(s, l_start=i, r_start=i)
        for i in range(n - 1):
            palindromes += count_palindromes(s, l_start=i, r_start=i+1)
        return palindromes


def count_palindromes(s, *, l_start, r_start):
    n = len(s)
    r, l = r_start, l_start
    palindromes = 0
    while(r < n and l >= 0 and s[l] == s[r]):
        palindromes += 1
        r += 1
        l -= 1
    return palindromes

s = Solution()

input_1 = "abc"
expected_1 = 3
assert s.countSubstrings(input_1) == expected_1
input_2 = "aaa"
expected_2 = 6
assert s.countSubstrings(input_2) == expected_2


