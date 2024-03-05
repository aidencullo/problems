from collections import deque

from node import Node

def merge_sort(numbers: list[int]):
    if len(numbers) == 1:
        return numbers

    k = len(numbers) // 2

    return merge(merge_sort(numbers[:k]), merge_sort(numbers[k:]))

def merge(l, r):
    n = []
    while r and l:
        if r[0] <= l[0]:
            n.append(r.pop(0))
        else:
            n.append(l.pop(0))

    if r:
        n.extend(r)
    else:
        n.extend(l)

    return n
