import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def findPositions(arr, x):
  # Write your code here
    q = deque((pos + 1, num) for pos, num in enumerate(arr))
    res = []

    for i in range(x):
        update_q(q, x, res)
    return res

def update_q(q, x, res):
    i = 0
    cur_max = -math.inf
    popped = []
    while i < x and q:
        pos, cur = q.popleft()
        popped.append((pos, cur))
        if cur > cur_max:
            cur_max = cur
            max_idx = i
            original_max_idx = pos
        i += 1
    popped.pop(max_idx)
    popped = [(pos, num - 1) if num > 0 else (pos, num) for pos, num in popped]
    q.extend(popped)
    res.append(original_max_idx)

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
