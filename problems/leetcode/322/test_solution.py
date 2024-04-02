import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,5], 11,), 3),
        (([2], 3,), -1),
        (([1], 0,), 0),
        (([186,419,83,408], 6249,), 20),
    ]
)
def testSolution(test_input, expected):
    assert Solution().coinChange(*test_input) == expected
