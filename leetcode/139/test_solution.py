import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('leetcode', ['leet', 'code']), True),
        (('applepenapple', ['apple', 'pen']), True),
        (('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']), False),
        (('a', ['a']), True),
        (('a', ['b']), False),
        (('a', []), False),
        (('a', ['a', 'b']), True),
        (('a', ['b', 'a']), True),
        (('a', ['a', 'a']), True),
        (('ccbb', ['bc', 'cb']), False),
        (('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
          ['a','aa','aaa','aaaa','aaaaa','aaaaaa','aaaaaaa','aaaaaaaa','aaaaaaaaa','aaaaaaaaaa']), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().wordBreak(*test_input) == expected
