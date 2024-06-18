import math
from collections import Counter, defaultdict
# Add any extra import statements you may need here


# Add any helper functions you may need here


def min_length_substring(s, t):
  # Write your code here
    need = Counter(t)
    window = defaultdict(int)
    left = 0
    min_len = math.inf
    min_idx = 0
    cnt = 0
    for right, letter in enumerate(s):
        if window[letter] < need[letter]:
            cnt += 1
        window[letter] += 1
        while cnt == len(t):
            if right - left + 1 < min_len:
                min_idx = left
                min_len = right - left + 1
            if window[s[left]] == need[s[left]]:
                cnt -= 1
            window[s[left]] -= 1
            left += 1
    return min_len if min_len != math.inf else -1










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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here

  s3 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t3 = "ffffff"
  expected_3 = 40
  output_3 = min_length_substring(s3, t3)
  check(expected_3, output_3)
  


  s4 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddfeff"
  t4 = "ff"
  expected_4 = 2
  output_4 = min_length_substring(s4, t4)
  check(expected_4, output_4)
  
