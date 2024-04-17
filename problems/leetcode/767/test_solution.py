import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (('aab',), 'aba'),
    (('aaab',), ''),
    (("baaba",), 'ababa'),
])
def test_solution(test_input, expected):
    assert Solution().reorganizeString(*test_input) == expected
