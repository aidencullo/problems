from solution import Solution


def test_countConsistentStrings():
    solution = Solution()
    
    # Test case 1
    allowed = "ab"
    words = ["ad", "bd", "aaab", "baa", "badab"]
    assert solution.countConsistentStrings(allowed, words) == 2
    
    # Test case 2
    allowed = "abc"
    words = ["a", "b", "c", "ab", "ac", "bc", "abc"]
    assert solution.countConsistentStrings(allowed, words) == 7
    
    # Test case 3
    allowed = "cad"
    words = ["cc", "acd", "b", "ba", "bac", "bad", "ac", "d"]
    assert solution.countConsistentStrings(allowed, words) == 4

    # Additional test case 1
    allowed = "xyz"
    words = ["x", "y", "z", "xy", "xz", "yz", "xyz"]
    assert solution.countConsistentStrings(allowed, words) == 7
    
    # Additional test case 2
    allowed = "mnop"
    words = ["m", "n", "o", "p", "mn", "op", "mnop", "nmop", "pmno"]
    assert solution.countConsistentStrings(allowed, words) == 9
