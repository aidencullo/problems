import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def balancedSplitExists(arr):
  # Write your code here
    arr.sort()
    total = sum(arr)
    running = 0
    for i, el in enumerate(arr):
        running += el
        if running == (total / 2):            
            return el != arr[i + 1]
    return False










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
  arr_1 = [2, 1, 2, 5]
  expected_1 = True
  output_1 = balancedSplitExists(arr_1)
  check(expected_1, output_1)

  arr_2 = [3, 6, 3, 4, 4]
  expected_2 = False
  output_2 = balancedSplitExists(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
  arr_3 = [3, 6, 3, 4, 4, 1, 4]
  expected_3 = False
  output_3 = balancedSplitExists(arr_3)
  check(expected_3, output_3)
  
  arr_4 = [4, 4, 4, 4, 4, 4]
  expected_4 = False
  output_4 = balancedSplitExists(arr_4)
  check(expected_4, output_4)
