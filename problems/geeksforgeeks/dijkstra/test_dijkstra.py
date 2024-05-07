import pytest
from dijkstra import Solution  

class TestSolution:
    @pytest.fixture
    def solution(self):
        return Solution()

    def test_dijkstra(self, solution):
        
        V = 2
        adj = [
            [[1, 9]],
            [[0, 9]],
        ]
        S = 0  
        
        distances = solution.dijkstra(V, adj, S)

        assert distances == [0, 9]
