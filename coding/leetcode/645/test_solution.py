import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 2, 2, 4], ), [2, 3]),
        (([1, 1], ), [1, 2]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().findErrorNums(*test_input) == expected
