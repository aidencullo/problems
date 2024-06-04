import pytest

from solution import Solution


@pytest.mark.parametrize("test_input, expected", [
    (("abc", "bac"), 2),
    (("abcde", "edbac"), 12),
])
def test_solution(test_input, expected):
    s = Solution()
    assert s.findPermutationDifference(*test_input) == expected
