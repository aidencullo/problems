import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((('abcdefd', 'd'), 'dcbaefd')),
        ((('xyxzxe', 'z'), 'zxyxxe')),
        ((('abcd', 'z'), 'abcd')),
    ],
)
def test_solution(test_input, expected):
    assert Solution().reversePrefix(*test_input) == expected
