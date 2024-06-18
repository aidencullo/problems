import pytest
from solution import Solution  # Assuming your solution file is named solution_file.py

# Initialize Solution class once for all tests
solution = Solution()

# Test cases
@pytest.mark.parametrize("word1, word2, expected", [
    ("abc", "pqr", "apbqcr"),
    ("ab", "pqrs", "apbqrs"),
    ("abcd", "pq", "apbqcd"),
    ("a", "xyz", "axyz"),
    ("", "abc", "abc"),
    ("abc", "", "abc"),
    ("", "", ""),
    ("x", "yz", "xyz"),
    ("hello", "world", "hweolrllod"),
    ("short", "longerstring", "slhoerngtsertring")
])
def test_mergeAlternately(word1, word2, expected):
    assert solution.mergeAlternately(word1, word2) == expected

# Additional test cases (optional)
def test_edge_cases():
    # Add any additional edge cases you might think of
    assert solution.mergeAlternately("a", "", "a") == "a"
    assert solution.mergeAlternately("", "a", "a") == "a"
    assert solution.mergeAlternately("", "", "") == ""

# Add more tests as needed

if __name__ == "__main__":
    pytest.main()
