class Solution:
    def minTimeToType(self, word: str) -> int:
        def move_to(start: str, end: str):
            diff = abs(ord(end) - ord(start))
            return min(diff, 26 - diff)

        time = 0
        last = 'a'
        for c in word:
            time += move_to(last, c)
            last = c

        time += len(word)        
        return time