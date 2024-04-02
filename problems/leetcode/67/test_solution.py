import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('11', '1'), '100'),
        (('11', '11'), '110'),
        (('100', '100'), '1000'),
        (('0', '0'), '0'),
    ]
)
def testSolution(test_input, expected):
    assert Solution().addBinary(*test_input) == expected
