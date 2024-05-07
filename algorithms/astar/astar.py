from typing import Dict, List, Optional, Tuple

AdjacencyList = Dict[str, Dict[str, int]]


class AStar:
    def __init__(self, graph: Optional[AdjacencyList] = None):
        if graph is None:
            graph = {}
        self.graph = graph

    def find_path(self, start: str, end: str) -> List[str]:
        pass
