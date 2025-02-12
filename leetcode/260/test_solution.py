import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (([1,2,1,3,2,5], ), [3,5]),
        (([-1,0], ), [-1,0]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().singleNumber(*test_input) == expected or Solution().singleNumber(*test_input)[::-1] == expected
