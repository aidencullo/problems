import pytest
from solution import Solution

@pytest.mark.parametrize("input_string, expected_output", [
    ("tree", "eetr"),
    ("cccaaa", "cccaaa"),
    ("Aabb", "bbAa")
])
def test_sort_string(input_string, expected_output):
    assert Solution().frequencySort(input_string) == expected_output

@pytest.mark.parametrize("input_string, expected_output", [
    ("tree", "eetr"),
    ("Aabb", "bbAa"),
    ("loveleetcode", "eeeeoovlltcd")
])
def test_sort_string_alternate(input_string, expected_output):
    assert Solution().frequencySort(input_string) == expected_output
