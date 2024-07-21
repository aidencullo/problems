from solution import Solution

def test_find_the_winner():
    sol = Solution()

    # Test case 1
    n = 5
    k = 2
    result = sol.findTheWinner(n, k)
    expected = 3
    assert result == expected
