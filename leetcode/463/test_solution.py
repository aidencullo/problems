import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]],), 16),
        (([[1]],), 4),
        (([[1, 0]],), 4),
    ],
)
def test_solution(test_input, expected):
    assert Solution().islandPerimeter(*test_input) == expected
