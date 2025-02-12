import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([4,5,6,7,0,1,2], 0), 4),
        (([4,5,6,7,0,1,2], 3), -1),
        (([1], 0), -1),
        (([5,1,3], 5), 0),
    ]
)
def testSolution(test_input, expected):
    assert Solution().search(*test_input) == expected
