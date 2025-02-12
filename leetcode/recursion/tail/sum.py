def sum_non_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    if not ls:
        return 0
    return ls.pop() + sum_non_tail_recursion(ls)

def sum_tail_recursion(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    def helper(running_total, ls):
        if not ls:
            return running_total
        return helper(running_total + ls.pop(), ls)
    return helper(0, ls)


def sum_tail_recursion_stack(ls):
    """
    :type ls: List[int]
    :rtype: int, the sum of the input list.
    """
    stack = [0]
    while ls:
        running = stack.pop()
        running += ls.pop()
        stack.append(running)
    return stack[-1]

assert sum_non_tail_recursion([1, 2, 3, 4, 5]) == 15
assert sum_tail_recursion([1, 2, 3, 4, 5]) == 15
assert sum_non_tail_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
assert sum_tail_recursion([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 55
assert sum_tail_recursion_stack([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]) == 210
