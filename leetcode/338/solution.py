class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = [0]
        for x in range(1, n + 1):
            bits.append(bits[x // 2] + (x & 1))
        return bits
