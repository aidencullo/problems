import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((3, [[0, 1], [1, 2], [2, 0]], 0, 2), True),
        ((6, [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], 0, 5), False),
    ],
)
def test_solution(test_input, expected):
    assert Solution().validPath(*test_input) == expected

