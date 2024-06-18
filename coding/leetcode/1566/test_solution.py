import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,4,4,4,4], 1, 3), True),
        (([1,2,1,2,1,1,1,3], 2, 2), True),
        (([1,2,1,2,1,3], 2, 3), False),
    ],
)
def test_solution(test_input, expected):
    assert Solution().containsPattern(*test_input) == expected
