def solution(A):
    A = [a for a in A if a > 0]
    A.sort()
    if not A:
        return 1
    if A[0] > 1:
        return 1
    last = None
    for a in A:
        if last and a - last > 1:
            return last + 1
        last = a
    return last + 1
