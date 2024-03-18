import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([2,3,6,7], 7), [[2,2,3],[7]]),
        (([2], 1), []),
    ]

)
def testSolution(test_input, expected):
    assert Solution().combinationSum(*test_input) == expected
