import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([2, 2, 3, 2], ), 3),
        (([0, 1, 0, 1, 0, 1, 99], ), 99),
        (([-2,-2,1,1,4,1,4,4,-4,-2], ), -4),
    ],
)
def test_solution(test_input, expected):
    assert Solution().singleNumber(*test_input) == expected
