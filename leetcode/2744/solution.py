class Solution:
    def maximumNumberOfStringPairs(self, words: list[str]) -> int:
        seen = set()
        total = 0
        for word in words:
            if word[::-1] in seen:
                seen.remove(word[::-1])
                total += 1
            seen.add(word)
        return total
