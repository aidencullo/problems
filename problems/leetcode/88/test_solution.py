import pytest

from solution import Solution

@pytest.mark.parametrize("test_input, expected", [
    (([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6]),
    (([1], 1, [], 0), [1]),
    (([0], 0, [1], 1), [1]),
])
def test_solution(test_input, expected):
    nums1, m, nums2, n = test_input
    Solution().merge(*test_input)
    assert nums1 == expected
