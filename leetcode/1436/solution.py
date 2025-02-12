class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        d = dict(paths)
        departures = d.keys()
        arrivals = d.values()
        return (set(arrivals) - set(departures)).pop()
