from typing import List

def next_tallest(heights: List[int]):
    stack = []
    next_highest = []
    for height in heights[::-1]:
        while stack and stack[-1] <= height:
            stack.pop()
        if stack:
            next_highest.append(stack[-1])
        else:
            next_highest.append(-1)
        stack.append(height)
    return next_highest[::-1]

import pytest

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([2,1,2,4,3],), [4,2,4,-1,-1]),
        (([5,4,3,2,1],), [-1,-1,-1,-1,-1]),
        (([1,2,3,4,5],), [2,3,4,5,-1]),
    ]
)
def testSolution(test_input, expected):
    actual = next_tallest(*test_input)
    assert actual == expected
