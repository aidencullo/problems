# time complexity: O(n)
# space complexity: O(n)

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
DIGIT_BASE = ord('0')
DIGIT_RANGE = ord('9') - DIGIT_BASE + 1
UPPERCASE_BASE = ord('A')
UPPERCASE_RANGE = ord('Z') - UPPERCASE_BASE + 1
LOWERCASE_BASE = ord('a')
LOWERCASE_RANGE = ord('z') - LOWERCASE_BASE + 1

def rotate_digit(char, factor):
    return rotate(char, DIGIT_BASE, DIGIT_RANGE, factor)

def rotate_uppercase(char, factor):
    return rotate(char, UPPERCASE_BASE, UPPERCASE_RANGE, factor)

def rotate_lowercase(char, factor):
    return rotate(char, LOWERCASE_BASE, LOWERCASE_RANGE, factor)

def rotate(char, base, range, factor):
    char_ascii = ord(char)
    char_offset = char_ascii - base
    char_local = char_offset + factor
    char_index = char_local % range
    char_rotated = base + char_index
    char_str = chr(char_rotated)
    return char_str

def cipher(input_char, factor):
    if input_char.isdigit():
      return rotate_digit(input_char, factor)
    if input_char.isupper():
      return rotate_uppercase(input_char, factor)
    if input_char.islower():
      return rotate_lowercase(input_char, factor)
    return input_char

def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  res = [cipher(l, rotation_factor) for l in input_str]
  return ''.join(res)




# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  input_1 = "All-convoYs-9-be:Alert1."
  rotation_factor_1 = 4
  expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
  output_1 = rotationalCipher(input_1, rotation_factor_1)
  check(expected_1, output_1)

  input_2 = "abcdZXYzxy-999.@"
  rotation_factor_2 = 200
  expected_2 = "stuvRPQrpq-999.@"
  output_2 = rotationalCipher(input_2, rotation_factor_2)
  check(expected_2, output_2)

  # Add your own test cases here
  

  input_3 = "abcdZXYzxy-999.@"
  rotation_factor_3 = 0
  expected_3 = "abcdZXYzxy-999.@"
  output_3 = rotationalCipher(input_3, rotation_factor_3)
  check(expected_3, output_3)

  input_4 = "abcdZXYzxy-999.@"
  rotation_factor_4 = 26
  expected_4 = "abcdZXYzxy-555.@"
  output_4 = rotationalCipher(input_4, rotation_factor_4)
  check(expected_4, output_4)
