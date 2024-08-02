from solution import Solution

def test_kthPalindrome():
    sol = Solution()
    assert sol.kthPalindrome([1,2,3,4,5,90], 3) == [101,111,121,131,141,999]
    assert sol.kthPalindrome([2,4,6], 4) == [1111,1331,1551]
    assert sol.kthPalindrome([2,201429812,8,520498110,492711727,339882032,462074369,9,7,6], 1) == []
    assert sol.kthPalindrome([
    
# Example 1:

# Input: queries = [1,2,3,4,5,90], intLength = 3
# Output: [101,111,121,131,141,999]
# Explanation:
# The first few palindromes of length 3 are:
# 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
# The 90th palindrome of length 3 is 999.
# Example 2:

# Input: queries = [2,4,6], intLength = 4
# Output: [1111,1331,1551]
# Explanation:
# The first six palindromes of length 4 are:
# 1001, 1111, 1221, 1331, 1441, and 1551.
 
