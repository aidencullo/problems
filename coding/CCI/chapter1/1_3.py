# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,and that you are given the "true" length of the string. (Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20John%20Smith" Hints: #53, #118

# ########## O(n) time O(n) space

# def solution(txt: str, real_size: int) -> str:
#     real_txt = txt[:real_size]
#     words = real_txt.split(' ')
#     return '%20'.join(words)

# ########## O(n) time O(1) space
# had to convert str into list[str] since strings are immutable in Python


def solution(txt: str, real_size: int) -> str:
    txt = list(txt)
    spaces = 0
    for letter in txt:
        if letter == ' ':
            spaces += 1
    spaces /= 3

    end_of_word = real_size - 1
    end_of_txt = len(txt) - 1
    while end_of_word > 0:
        if txt[end_of_word] == ' ':
            txt[end_of_txt] = '0'
            txt[end_of_txt - 1] = '2'
            txt[end_of_txt - 2] = '%'
            end_of_txt -= 3
        else:
            txt[end_of_txt] = txt[end_of_word]
            end_of_txt -= 1
        end_of_word -= 1
    return ''.join(txt)
        

import pytest

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('Mr John Smith    ', 13), 'Mr%20John%20Smith'),
        (('Mr John  ', 7), 'Mr%20John'),
        (('Mr   ', 3), 'Mr%20'),
        (('', 0), ''),
    ],
)
def test(test_input, expected):
    assert solution(*test_input) == expected
