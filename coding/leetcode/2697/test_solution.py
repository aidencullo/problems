# test_solution.py

import pytest
from solution import Solution

# Instantiate the Solution class
solution = Solution()

def test_makeSmallestPalindrome():
    # Test case 1: Example from problem statement
    assert solution.makeSmallestPalindrome("egcfe") == "efcfe"

    # Test case 2: Minimum length string
    assert solution.makeSmallestPalindrome("a") == "a"

    # Test case 3: Longer palindrome
    assert solution.makeSmallestPalindrome("abba") == "abba"

    # Test case 4: Palindrome already, no change needed
    assert solution.makeSmallestPalindrome("racecar") == "racecar"

    # Test case 7: Edge case - empty string
    assert solution.makeSmallestPalindrome("") == ""

    # Test case 8: Edge case - all identical characters
    assert solution.makeSmallestPalindrome("aaaa") == "aaaa"

    # Test case 10: Edge case - single character repeated
    assert solution.makeSmallestPalindrome("zzzzzzzz") == "zzzzzzzz"

    # Test case 11: Edge case - mix of characters needing minimal changes
    assert solution.makeSmallestPalindrome("abcdefghijkllkjihgfedcba") == "abcdefghijkllkjihgfedcba"

# You can add more test cases as needed
