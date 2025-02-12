import pytest

from solution import Solution

@pytest.mark.parametrize(
    ('test_input', 'expected'),
    [
        (('a', 'b'), False),
        (('aa', 'ab'), False),
    ]
)
def testSolution(test_input, expected):
    assert Solution().canConstruct(*test_input) == expected
