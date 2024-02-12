from itertools import permutations

s = 'abc'
B = 'dadabcab'
size = len(s)
count = 0

def my_permutations(x):
    for permutation in permutations(x):
        yield ''.join(permutation)

hash_map = dict.fromkeys(my_permutations(s))

for index, el in enumerate(B[:-(size-1)]):
    if B[index: index + size] in hash_map:
        count += 1

print(f'{count==3}')
