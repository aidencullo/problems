import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here


def minOperations(arr):
  # Write your code here
    n = len(arr)
    target = list(range(1, n + 1))
    src = deque([arr])
    dest = deque([target])
    src_visited = []
    src_steps = -1
    dest_visited = []
    dest_steps = -1

    while src and dest:
        src_steps += 1
        for __ in range(len(src)):
            node = src.popleft()
            if node in dest_visited:
                return src_steps + dest_steps
            src_visited.append(node)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    reversed_node = node[:i] + node[i:j][::-1] + node[j:]
                    if not reversed_node in src_visited:
                        src.append(reversed_node)            

        

        dest_steps += 1
        for __ in range(len(dest)):
            node = dest.popleft()
            if node in src_visited:
                return src_steps + dest_steps
            dest_visited.append(node)
            for i in range(n):
                for j in range(i + 1, n + 1):
                    reversed_node = node[:i] + node[i:j][::-1] + node[j:]
                    if not reversed_node in dest_visited:
                        dest.append(reversed_node)










# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  n_1 = 5
  arr_1 = [1, 2, 5, 4, 3]
  expected_1 = 1
  output_1 = minOperations(arr_1)
  check(expected_1, output_1)

  n_2 = 3
  arr_2 = [3, 1, 2]
  expected_2 = 2
  output_2 = minOperations(arr_2)
  check(expected_2, output_2)
  
  # Add your own test cases here

  n_3 = 10
  arr_3 = list(range(1, 11))[::-1]
  expected_3 = 1
  output_3 = minOperations(arr_3)
  check(expected_3, output_3)
  
