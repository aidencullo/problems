import pytest

from solution import Solution

@pytest.mark.parametrize(
    "test_input,expected",
    [
        (('{}]()',), False),
        (('([{}])',), True),
        (('{}[]()',), True),
        (('{}',), True),
        (('[]',), True),
        (('()',), True),
    ],
)
def test(test_input, expected):
    s = Solution()
    assert s.isValid(*test_input) == expected
