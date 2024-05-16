import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (("(1+(2*3)+((8)/4))+1", ), 3),
    ],
)
def test_solution(test_input, expected):
    assert Solution().maxDepth(*test_input) == expected
