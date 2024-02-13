# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
# Hints: #44, #7 7 7, #732

########## O(n) time and space

# import pytest

# def is_unique(s):
#     hash_map = {}
#     for letter in s:
#         if letter in hash_map:
#             return False
#         hash_map[letter] = None
#     return True
    
########## O(n log n) time and O(1) space

# def is_unique(s):
#     s_sorted = sorted(s)
#     last = s_sorted.pop()
#     while s_sorted:
#         current = s_sorted.pop()
#         if last == current:
#             return False
#         last = current
#     return True

########## O(n) time and O(1) space

def is_unique(s):
    bit_vector = 0
    for letter in s:
        if (1 << ord(letter)) & bit_vector:
            return False
        letter_bit_vector = (1 << ord(letter))
        bit_vector |= letter_bit_vector
    return True 

import pytest

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ('acv', True),
        ('aac', False),
        ('absdl', True),
        ('a', True),
    ],
)
def test(test_input, expected):
    assert is_unique(test_input) == expected
