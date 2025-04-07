class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for x in range(n + 1):
            total = 0
            while x > 0:
                total += x & 1
                x =// 2
            bits.append(total)
        return bits
