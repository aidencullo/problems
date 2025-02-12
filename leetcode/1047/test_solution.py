import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("abbaca", ), "ca"),
        (("azxxzy", ), "ay"),
    ],
)
def test_solution(test_input, expected):
    assert Solution().removeDuplicates(*test_input) == expected
