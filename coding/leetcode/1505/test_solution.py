import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("4321", 4), "1342"),
    ],
)
def test_solution(test_input, expected):
    assert Solution().minInteger(*test_input) == expected
