from collections import deque

from node import Node

def quicksort(numbers: list[int]):
    if len(numbers) == 1 or len(numbers) == 0:
        return numbers

    k = numbers[0]
    l = []
    r = []

    for n in numbers[1:]:
        if n <= k:
            l.append(n)
        else:
            r.append(n)

    return quicksort(l) + [k] + quicksort(r)
