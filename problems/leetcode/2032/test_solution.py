import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 1, 2, 2, 3], [2, 3], [3]), [2, 3]),
        (([3, 1], [2, 3], [1, 2]), [1, 2, 3]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().twoOutOfThree(*test_input) == expected
