import pytest
from astar import AStar

class TestAStar:
    def test_simple_case(self):
        # Define a simple graph
        graph = {
            'A': {'B': 1, 'C': 3},
            'B': {'A': 1, 'D': 5},
            'C': {'A': 3, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        
        # Instantiate the AStar class
        astar = AStar(graph)
        
        # Test case: shortest path from 'A' to 'D' should be 'A' -> 'B' -> 'D'
        assert astar.find_path('A', 'D') == ['A', 'B', 'D']
        
    def test_no_path(self):
        # Define a graph with no path between two nodes
        graph = {
            'A': {'B': 1},
            'B': {'C': 1},
            'C': {'D': 1},
            'D': {}
        }
        
        # Instantiate the AStar class
        astar = AStar(graph)
        
        # Test case: There should be no path from 'A' to 'D'
        assert astar.find_path('A', 'D') is None

    # Add more test cases as needed...
