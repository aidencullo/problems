import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('aaa', 'aaa'), True),
        (('ab', 'ab'), True),
        (("leetcode", "yyyyyyyylyyyyyeyyyyyyyyyeyyyyyyyyytyyyyycyyyyoyyyyyyyyydyyyyyyyyeyyyyyyyyy"), True),
        (('abc', 'ahbgdc'), True),
        (('axc', 'ahbgdc'), False),
        (('ab', 'ba'), False),
        (('ab', 'baa'), False),
        (('ab', 'baaa'), False),
        (('ab', 'baaaa'), False),
        (('ab', 'baaaaa'), False),
        (('ab', 'baaaaaa'), False),
        (('ab', 'baaaaaaa'), False),
        (('ab', 'baaaaaaaa'), False),
        (('', 'ahbgdc'), True),
        (("aaaaaa", "bbaaaa"), False),
        
    ],
)
def test_solution(test_input, expected):
    assert Solution().isSubsequence(*test_input) == expected
