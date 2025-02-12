import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1, 2, 3], ), [1, 2, 4]),
        (([4, 3, 2, 1], ), [4, 3, 2, 2]),
        (([0], ), [1]),
        (([9], ), [1, 0]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().plusOne(*test_input) == expected
