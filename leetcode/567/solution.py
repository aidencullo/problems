class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        ht1 = [0] * 26
        ht2 = [0] * 26

        for i in range(len(s1)):
            ht1[ord(s1[i]) - ord('a')] += 1
            ht2[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 if ht1[i] == ht2[i] else 0 for i in range(26))

        for i in range(len(s1), len(s2)):
            if matches == 26:
                return True
            index = ord(s2[i]) - ord('a')
            ht2[index] += 1
            if ht1[index] == ht2[index]:
                matches += 1
            elif ht1[index] == ht2[index] - 1:
                matches -= 1
            index = ord(s2[i - len(s1)]) - ord('a')
            ht2[index] -= 1
            if ht1[index] == ht2[index]:
                matches += 1
            elif ht1[index] == ht2[index] + 1:
                matches -= 1
        return matches == 26
