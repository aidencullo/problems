import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((1, 1), 0),
        ((2, 1), 0),
        ((2, 2), 1),
        ((4, 5), 1),
    ],
)
def test_solution(test_input, expected):
    assert Solution().kthGrammar(*test_input) == expected
