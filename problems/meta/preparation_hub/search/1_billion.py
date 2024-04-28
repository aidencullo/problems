import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
def binary_search(arr, l, r):
    while l <= r:
        k = (l + r) // 2
        target = sum(rate ** k for rate in arr)
        if target == 1000000000:
            return k
        if target < 1000000000:
            l = k + 1
        else:
            r = k - 1
    return l



def getBillionUsersDay(growthRates):
  # Write your code here
    i = 0
    min_square = 0
    max_square = 0
    while True:
        if sum(rate ** (i ** 2) for rate in growthRates) >= 1000000000:
            max_square = i ** 2
            break
        min_square = i ** 2
        i += 1
    return binary_search(growthRates, min_square, max_square)












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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  
