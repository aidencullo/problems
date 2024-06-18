import heapq

class Solution:
    def dijkstra(self, V, adj, S):
        paths = [float('inf')] * V
        pq = [(0, S)]
        visited = set()

        while pq:
            distance, node = heapq.heappop(pq)
            visited.add(node)
            if distance < paths[node]:
                paths[node] = distance
            for neighbor, weight in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(pq, (distance + weight, neighbor))
        return paths
