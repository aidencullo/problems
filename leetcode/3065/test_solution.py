import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([2,11,10,1,3], 10), 3),
        (([1,1,2,4,9], 1), 0),
        (([1,1,2,4,9], 9), 4),
    ],
)
def test_solution(test_input, expected):
    assert Solution().minOperations(*test_input) == expected
