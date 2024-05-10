import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (("mississippi", "issip"), 4),
    (("leetcode", "leeto"), -1),
    (("sadbutsad", "sad"), 0),
])
def test_solution(test_input, expected):
    assert Solution().strStr(*test_input) == expected
