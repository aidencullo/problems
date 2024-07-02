import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([0, 1, 2, 3, 4, 5, 6, 7, 8],), [0, 1, 2, 4, 8, 3, 5, 6, 7]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().sortByBits(*test_input) == expected
