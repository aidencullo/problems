import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def rotationalCipher(input_str, rotation_factor):
  # Write your code here
  digit_base = ord('0')
  digit_range = ord('9') - digit_base + 1
  uppercase_base = ord('A')
  uppercase_range = ord('Z') - uppercase_base + 1
  lowercase_base = ord('a')
  lowercase_range = ord('z') - lowercase_base + 1
  res = []
  for character in input_str:
    char_ascii = ord(character)
    if character.isalnum():
      if character.isdigit():
        char_ascii -= digit_base
        character = chr(digit_base + (char_ascii + rotation_factor) % digit_range)
      elif character.isupper():
        char_ascii -= uppercase_base
        character = chr(uppercase_base + (char_ascii + rotation_factor) % uppercase_range)
      else:
        char_ascii -= lowercase_base
        character = chr(lowercase_base + (char_ascii + rotation_factor) % lowercase_range)
    res.append(character)
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
  
