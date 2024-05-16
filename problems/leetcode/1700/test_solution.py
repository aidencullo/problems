import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 1, 0, 0], [0, 1, 0, 1]), 0),
        (([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]), 3),
    ],
)
def test_solution(test_input, expected):
    assert Solution().countStudents(*test_input) == expected
