import pytest

from solution import Solution


@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((8,), 4),
        ((14,), 6),
        ((123,), 12),
        ((0,), 0),
    ],
)
def test_solution(test_input, expected):
    assert Solution().numberOfSteps(*test_input) == expected
