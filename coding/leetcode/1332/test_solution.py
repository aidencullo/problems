import pytest
from solution import Solution

# Test cases
@pytest.mark.parametrize("s, expected", [
    ("ababa", 1),
    ("abb", 2),
    ("baabb", 2),
    ("racecar", 1),  # Additional test case for a longer palindrome
    ("", 0),         # Edge case: empty string
    ("ab", 2),       # Edge case: non-palindromic string
    ("aaa", 1),      # Edge case: all characters are the same
    ("abcdcba", 1)   # Edge case: longest palindrome
])
def test_removePalindromeSub(s, expected):
    assert Solution().removePalindromeSub(s) == expected

# Additional tests (optional)
def test_additional_cases():
    # Add any additional test cases you might want to include
    assert Solution().removePalindromeSub("abcabc") == 2
    assert Solution().removePalindromeSub("xyzzyx") == 1

if __name__ == "__main__":
    pytest.main()
