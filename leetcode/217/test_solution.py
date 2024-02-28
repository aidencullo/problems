import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,3,1],), True),
        (([1,2,3],), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().containsDuplicate(*test_input) == expected
