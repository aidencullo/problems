import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("string"), "rtsng"),
    (("poiinter"), "ponter"),
])
def test_solution(test_input, expected):
    assert Solution().finalString(test_input) == expected
