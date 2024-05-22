class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        potential_judges = set(range(1, n + 1))
        for truster, trustee in trust:
            if truster in potential_judges:
                potential_judges.remove(truster)
        if len(potential_judges) != 1:
            return -1
        judge = list(potential_judges)[0]
        trusters = sum([1 if trustee == judge else 0 for truster, trustee in trust])
        if trusters == n - 1:
            return judge
        return -1
