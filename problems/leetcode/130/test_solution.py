import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((43261596, ), 964176192),
        ((4294967293, ), 3221225471),
    ],
)
def test_solution(test_input, expected):
    assert Solution().reverseBits(*test_input) == expected
