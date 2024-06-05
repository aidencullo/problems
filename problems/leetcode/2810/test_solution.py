import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("abc"), "abc"),
    (("abci"), "cba"),
    (("string"), "rtsng"),
    (("poiinter"), "ponter"),
])
def test_solution(test_input, expected):
    assert Solution().finalString(test_input) == expected
