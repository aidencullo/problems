import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,8,6,2,5,4,8,3,7],), 49),
        (([1,1],), 1),
        (([4,3,2,1,4],), 16),
        (([1,2,1],), 2),
        (([2,3,10,5,7,8,9], ), 36),
    ]
)
def testSolution(test_input, expected):
    actual = Solution().maxArea(*test_input)
    assert actual == expected

def compare_arrays(a, b):
    assert len(a) == len(b)
    for i in range(len(a)):
        assert a[i] == b[i]
