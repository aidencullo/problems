import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([2,7,11,15], 9), [1,2]),
    ]
)
def testSolution(test_input, expected):
    assert Solution().twoSum(*test_input) == expected
