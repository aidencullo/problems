# import pytest

# from solution import Solution


# @pytest.mark.parametrize("test_input, expected", [
#     (("the quick brown fox jumps over the lazy dog", "vkbs bs t suepuv"), "this is a secret"),
#     (("eljuxhpwnyrdgtqkviszcfmabo", "zwx hnfx lqantp mnoeius ycgk vcnjrdb"), "the five boxing wizards jump quickly"),
# ])
# def test_solution(test_input, expected):
#     s = Solution()
#     assert s.decodeMessage(*test_input) == expected


from solution import OrderedStream


def test_solution():
    s = OrderedStream(5)
    assert s.insert(3, "ccccc") == []
    assert s.insert(1, "aaaaa") == ["aaaaa"]
    assert s.insert(2, "bbbbb") == ["bbbbb", "ccccc"]
    assert s.insert(5, "eeeee") == []
    assert s.insert(4, "ddddd") == ["ddddd", "eeeee"]
