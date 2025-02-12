import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([3, 0, 1],), 2),
        (([0, 1],), 2),
        (([9, 6, 4, 2, 3, 5, 7, 0, 1],), 8),
        (([0],), 1),
    ],
)
def test_solution(test_input, expected):
    assert Solution().missingNumber(*test_input) == expected
