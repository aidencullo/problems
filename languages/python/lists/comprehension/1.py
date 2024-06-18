"""Ins and Outs of Python Lists/Matrices"""

# list comp from numbers list
import math

numbers = list(range(100))
squares_of_evens = [n**2 for n in numbers if not n % 2]
# verify
all(not math.sqrt(square) % 2  for square in squares_of_evens)

