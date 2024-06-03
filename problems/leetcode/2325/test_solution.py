import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"), "this is a secret"),
    (("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"), "the five boxing wizards jump quickly"),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.decodeMessage(*test_input) == expected
