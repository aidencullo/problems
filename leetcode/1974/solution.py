class Solution:
    def minTimeToType(self, word: str) -> int:
        def move_to(start: str, end: str):
            forward = ord(end) - ord(start)
            forward = forward if forward >= 0 else forward + 26
            backward = ord(start) - ord(end)
            backward = backward if backward >= 0 else backward + 26
            return min(forward, backward)

        time = 0
        current = 'a'
        for c in word:
            time += move_to(current, c)
            time += 1
            current = c
        return time