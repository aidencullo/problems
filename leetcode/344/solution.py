class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        last_index = n - 1
        k = n // 2
        for i in range(k):
            s[i], s[last_index - i] = s[last_index - i], s[i]


"""
idea

iterate to len // 2 (?) -- off by one error?
swapping i with len - i
- something like this, there is an off by one surely


examples:

n = 4
indices = 0,1,2,3
k = 2
range(k) = 0, 1

n = 5
indices = 0,1,2,3,4
k = 2
range(k) = 0, 1

# corner cases

n = 1 ( can't have 0)
indices = 0
k = 0
range(k) = 

n = 2
indices = 0, 1
k = 1
range(k) = 0

Constraints:

1 <= s.length <= 10 ** 5
s[i] is a printable ascii character.
- does this mean we can use constant mem array to hold/track chars?
"""
