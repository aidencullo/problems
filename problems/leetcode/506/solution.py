class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        scores_sorted = sorted(score, reverse=True)
        positions = { s: i + 1 for i, s in enumerate(scores_sorted) }
        for i in range(len(score)):
            p = positions[score[i]]
            if p == 1:
                yield "Gold Medal"
            elif p == 2:
                yield "Silver Medal"
            elif p == 3:
                yield "Bronze Medal"
            else:
                yield str(p)
