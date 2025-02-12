class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        def getMaxIntLength(k):
            if k % 2 == 0:
                return k // 2
            return k // 2  + 1

        def getMaxQuery(intLength):
            if intLength == 1:
                return 9
            return 9 * 10 ** (intLength - 1)
        
        def getKthPalindrome(query, n):
            m = getMaxIntLength(n)
            if query > getMaxQuery(m):
                return -1
            return 10 ** (m - 1) + query - 1

        def addOtherHald(palindrome):
            if palindrome == -1:
                return -1
            if intLength % 2 == 0:
                return int(str(palindrome) + str(palindrome)[::-1])
            return int(str(palindrome)[:-1] + str(palindrome)[::-1])
            
        
        res = [getKthPalindrome(query, intLength) for query in queries]
        res = [addOtherHald(p) for p in res]
        return res
