class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points = [x for x, y in points]
        points.sort()
        return max([abs(x - y) for x, y in zip(points, points[1:])])
