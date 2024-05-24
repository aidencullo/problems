import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((43261596,), 964176192),
    ],
)
def test_single_node(test_input, expected):
    result = Solution().reverseBits(*test_input)
    assert result == expected
