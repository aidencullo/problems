# time: O(n)
# space: O(1)
# n=number of digits in s

class Solution:
    def myAtoi(self, s: str) -> int:
        # remove leading and trailing whitespaces
        s_stripped = s.strip()

        # check if negative
        negative = is_negative(s_stripped)

        # strip negative or positive sign
        s_without_sign = strip_sign(s_stripped)

        # ignore non-digit characters
        s_only_digits = remove_non_digits(s_without_sign)

        # convert to integer
        s_int = convert_to_int(s_only_digits, negative)
        
        # cap at 32-bit signed integer
        s_max_32_bit = clamp_to_32_bit(s_int)

        return s_max_32_bit

def is_negative(s: str) -> bool:
    return s and s[0] == '-'

def strip_sign(s: str) -> str:
    if s and (s[0] == '-' or s[0] == '+'):
        return s[1:]
    return s

def remove_non_digits(s: str) -> str:
    for i, c in enumerate(s):
        if not c.isdigit():
            return s[:i]
    return s

def convert_to_int(s: str, negative: bool) -> int:
    try:
        s_int = int(s)
    except ValueError:
        return 0
    return s_int * (-1 if negative else 1)

def clamp_to_32_bit(n: int) -> int:
    if n < -2**31:
        return -2**31
    if n > 2**31 - 1:
        return 2**31 - 1
    return n
