import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("ababc", "ab"), 2),
        (("ababc", "ba"), 1),
        (("ababc", "ac"), 0),
        (("a", "a"), 1),
    ],
)
def test_solution(test_input, expected):
    assert Solution().maxRepeating(*test_input) == expected
