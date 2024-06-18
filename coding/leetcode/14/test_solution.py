import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((["flower","flow","flight"],), "fl"),
    ((["dog","racecar","car"],), ""),
    ((["dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog","dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog","dog","dog","dog","dog"],), "dog"),
    ((["dog","dog","dog","dog","dog","dog","dog","dog","dog"],), "dog"),
    ((["","dog","dog","dog","dog","dog","dog","dog","dog"],), ""),
    ((["ab", "a"],), "a"),
    ((["reflower","flow","flight"],), ""),
])
def test_solution(test_input, expected):
    assert Solution().longestCommonPrefix(*test_input) == expected
