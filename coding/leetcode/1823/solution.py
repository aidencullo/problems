class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = OrderedDict()
        for i in range(n):
            friends[i] = i + 1
        current = 0
        while len(friends) > 1:
            current = (current + (k - 1)) % len(friends)
            friends.pop(current)
        return friends[0]

from collections import OrderedDict
