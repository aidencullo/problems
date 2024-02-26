from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_counter = Counter(magazine)
        ransom_counter = Counter(ransomNote)
        difference_counter = magazine_counter.subtract(ransom_counter)
        return all(freq >= 0 for freq in magazine_counter.values())
