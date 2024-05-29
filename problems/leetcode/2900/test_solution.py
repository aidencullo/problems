import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        ((["e","a","b"], [0,0,1]), ["e","b"]),
        ((["a","b","c","d"], [1,0,1,1]), ["a","b","c"]),
    ],
)
def test_solution(test_input, expected):
    assert Solution().getLongestSubsequence(*test_input) == expected
