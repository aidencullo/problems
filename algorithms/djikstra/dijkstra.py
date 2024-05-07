import heapq
from typing import Dict

def dijkstra(graph: Dict[str, Dict[str, int]], start: str, end: str) -> int:
    paths = {vertex: float('inf') for vertex in graph}
    q = [(0, start)]
    visited = set()

    while q and end not in visited:
        distance, path = heapq.heappop(q)
        node = path[-1]
        if node == end:
            return (path, distance)
        if node in visited:
            continue
        visited.add(node)
        if distance < paths[node]:
            paths[node] = distance

        for neighbor in graph[node]:
            heapq.heappush(q, (distance + graph[node][neighbor], path + neighbor))
    return ('', float('inf'))
