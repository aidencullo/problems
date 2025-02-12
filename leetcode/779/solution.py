class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        m = k + 1
        return self.kthGrammar(n - 1, m // 2) ^ (m % 2)
