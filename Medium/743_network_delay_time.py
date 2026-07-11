from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        dist = [float('inf')] * n
        graph = [[] for _ in range(n)]
        visited = set()
        h = [(0, k)]
        dist[k-1] = 0

        for u, v, w in times:
            graph[u-1].append((v, w))

        while h:
            curr_cost, node = heapq.heappop(h)

            if node in visited:
                continue

            for neigh, price in graph[node-1]:
                if dist[neigh-1] > curr_cost + price:
                    heapq.heappush(h, (curr_cost + price, neigh))
                    dist[neigh-1] = curr_cost + price
            
            visited.add(node)
        
        maxiumum = max(dist)
        if maxiumum == float('inf'):
            return -1
        return maxiumum