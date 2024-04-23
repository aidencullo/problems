import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    ((["i", "love", "leetcode", "i", "love", "coding"], 2), ["i", "love"]),
    ((["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4), ["the", "is", "sunny", "day"]),
])
def test_solution(test_input, expected):
    assert Solution().topKFrequent(*test_input) == expected
