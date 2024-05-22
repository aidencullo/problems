class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        not_judges = set(truster for truster, trustee in trust)
        people = set(range(1, n + 1))
        if len(not_judges) != n - 1:
            return -1
        judge = people - not_judges
        judge = list(judge)[0]
        trusters = sum([1 if trustee == judge else 0 for truster, trustee in trust])
        if trusters == n - 1:
            return judge
        return -1
