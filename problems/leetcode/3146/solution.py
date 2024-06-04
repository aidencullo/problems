class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        t_dict = {letter: index for index, letter in enumerate(t)}
        return sum(abs(index - t_dict[letter]) for index, letter in enumerate(s))
