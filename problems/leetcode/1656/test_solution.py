import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"), "this is a secret"),
    (("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"), "the five boxing wizards jump quickly"),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.decodeMessage(*test_input) == expected


import pytest

from solution import OrderedStream


def test_solution():
    s = OrderedStream()
    assert s.insert(3, "ccccc") == []
    assert s.insert(1, "aaaaa") == ["aaaaa"]
    assert s.insert(2, "bbbbb") == ["bbbbb", "ccccc"]
    assert s.insert(5, "eeeee") == []
    assert s.insert(4, "ddddd") == ["ddddd", "eeeee"]




    Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]
