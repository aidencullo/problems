class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [l.lower() for l in s if l.isalnum()]
        middle = len(s) // 2
        first_half = s[:middle]
        if len(s) % 2 == 0:
            second_half = s[middle:][::-1]
        else:
            second_half = s[middle + 1:][::-1]
        return first_half == second_half

# other solution i saw that i wanted to implement -- i'm a fan

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = [l.lower() for l in s if l.isalnum()]
#         return s == s[::-1]
