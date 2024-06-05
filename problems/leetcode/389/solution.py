from functools import reduce


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = [ord(char) for char in s]
        s_xor = reduce(lambda x, y: x ^ y, s_list, 0)
        t_list = [ord(char) for char in t]
        t_xor = reduce(lambda x, y: x ^ y, t_list, 0)
        return chr(s_xor ^ t_xor)
