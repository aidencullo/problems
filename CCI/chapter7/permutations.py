import random

def permutations(prefix, rest):
    if len(rest) == 0:
        print(f'{prefix}')
    for index, letter in enumerate(rest):
        permutations(prefix + rest[index], rest[:index] + rest[index + 1:])
