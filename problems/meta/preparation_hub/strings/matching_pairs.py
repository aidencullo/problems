import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def matching_pairs(s, t):
  # Write your code here
    s = s.split()
    t = t.split()
    if s == t:
        return len(s) - 2
    pairs = sum(x == y for x, y in zip(s, t))
    for i, __ in enumerate(s):
        for j, __ in enumerate(s):
            if i != j:
                local_pairs = sum(s[k] == t[k] for k in [i, j])
                s[i], s[j] = s[j], s[i]
                local_pairs_new = sum(s[k] == t[k] for k in [i, j])
                pairs += local_pairs_new - local_pairs
    return pairs
        


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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here

  s_3, t_3 = "mno", "mno"
  expected_3 = 3
  output_3 = matching_pairs(s_3, t_3)
  check(expected_3, output_3)
  

  s_4, t_4 = "mnx", "mny"
  expected_4 = 1
  output_4 = matching_pairs(s_4, t_4)
  check(expected_4, output_4)
  

  s_5, t_5 = "abcde", "aecde"
  expected_5 = 4
  output_5 = matching_pairs(s_5, t_5)
  check(expected_5, output_5)
  
