import math
# Write any import statements here

def getUniformIntegerCountInInterval(A: int, B: int) -> int:
  # Write your code here
  current = A
  total = 0

  while True:
    current = findNextUniform(current)
    if current > B:
      break
    total += 1
    current += 1
  return total

def findNextUniform(number):
  if isUniform(number):
    return number
  nearbyUniform = uniformFromLeadingDigit(number)
  if number < nearbyUniform:
    return nearbyUniform
  uniformStep = nearbyUniform // int(str(nearbyUniform)[0])
  return nearbyUniform + uniformStep
  
def isUniform(number):
  numberStr = str(number)
  return all(digit == numberStr[0] for digit in numberStr)

def uniformFromLeadingDigit(number):
  numberStr = str(number)
  return int(''.join(list(numberStr[0] for digit in numberStr)))
