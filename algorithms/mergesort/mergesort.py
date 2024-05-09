from collections import deque

def mergesort(numbers: list[int]):
    if len(numbers) == 1:
        return numbers
    k = len(numbers) // 2
    l = mergesort(numbers[:k])
    r = mergesort(numbers[k:])
    return merge(l, r)

def merge(l: list[int], r: list[int]):
    sorted_numbers = []
    l = deque(l)
    r = deque(r)
    while l and r:
        if l[0] <= r[0]:
            sorted_numbers.append(l.popleft())
        else:
            sorted_numbers.append(r.popleft())
    sorted_numbers.extend(l or r)
    return sorted_numbers
