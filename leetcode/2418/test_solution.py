import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([[1, 2], [3], [3], []],), [[0, 1, 3], [0, 2, 3]]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().allPathsSourceTarget(*test_input) == expected
