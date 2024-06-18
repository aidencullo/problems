import pytest

from dijkstra import Solution  


class TestSolution:
    @pytest.mark.parametrize("vertices, graph, src, expected", [
        (2, [[[1, 9]], [[0, 9]]], 0, [0, 9]),
        (3, [[[1, 2], [2, 3]], [[0, 2], [2, 2]], [[0, 3], [1, 2]]], 0, [0, 2, 3]),
    ])
    def test_dijkstra(self, vertices, graph, src, expected):
        solution = Solution()
        distances = solution.dijkstra(vertices, graph, src)        
        assert distances == expected
