class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        scores_sorted = sorted(score, reverse=True)
        positions = {
            s: "Gold Medal" if i == 0 else
                "Silver Medal" if i == 1 else
                "Bronze Medal" if i == 2 else
                str(i + 1)
            for i, s
            in enumerate(scores_sorted)
        }
        return [positions[s] for s in score]
