from solution import Solution


def test_maxSubsequence():
    solution = Solution()

    # Test case 1
    nums = [3, 5, 2, 9, 7]
    k = 3
    expected = [5, 9, 7]
    result = solution.maxSubsequence(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"

    # Test case 2
    nums = [-1, -2, -3, -4, -5]
    k = 2
    expected = [-1, -2]
    result = solution.maxSubsequence(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"

    # Test case 3
    nums = [1, 2, 3, 4, 5]
    k = 5
    expected = [1, 2, 3, 4, 5]
    result = solution.maxSubsequence(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"

    # Test case 4
    nums = [10, -10, 10, -10, 10]
    k = 3
    expected = [10, 10, 10]
    result = solution.maxSubsequence(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"

    # Test case 5
    nums = [5]
    k = 1
    expected = [5]
    result = solution.maxSubsequence(nums, k)
    assert result == expected, f"Expected {expected} but got {result}"
