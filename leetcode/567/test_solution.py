import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('abc', 'xbaxyzabc'), True),
        (('ab', 'eidboaoo'), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().checkInclusion(*test_input) == expected
