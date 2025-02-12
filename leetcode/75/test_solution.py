import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([0,1,2],), [0,1,2]),
        (([1,0,2],), [0,1,2]),
        (([0,2,1],), [0,1,2]),
        (([0,2,1,1,2,0],), [0,0,1,1,2,2]),
    ]
)
def testSolution(test_input, expected):
    test_input, = test_input
    Solution().sortColors(test_input)
    assert test_input == expected
