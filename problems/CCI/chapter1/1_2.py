# Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.
# Hints: #7, #84, #722, #737

# ########## O(n log n) time O(1) space

# def solution(a, b):
#     return sorted(a) == sorted(b)
 
# ########## O(n) time O(1) space

# def solution(a, b):
#     hash_map = {}
#     for letter in a:
#         if letter in hash_map:
#             hash_map[letter] += 1
#         else:
#             hash_map[letter] = 1
#     for letter in b:
#         if letter not in hash_map:
#             return False
#         if letter in hash_map:
#             hash_map[letter] -= 1
#     for value in hash_map.values():
#         if value < 0:
#             return False
#     return True

########## O(n) time O(1) space, fewer lines

def solution(a, b):
    hash_map = {}
    for letter in a:
        hash_map.setdefault(letter, []).append(1)
    for letter in b:
        if letter not in hash_map or not hash_map[letter]:
            return False
        hash_map[letter].pop()
    return True

import pytest

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('aab', 'aba'), True),
        (('aab', 'xba'), False),
        (('aaba', 'aaab'), True),
        (('abcd', 'abdc'), True),
        (('a', 'a'), True),
    ],
)
def test(test_input, expected):
    assert solution(*test_input) == expected
