from collections import defaultdict
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        dist = {}
        h = [(-1, start_node)]

        for i, edge in enumerate(edges):
            u, v = edge
            prob = succProb[i]
            graph[u].append((v, prob))
            graph[v].append((u, prob))

        while h:
            curr_prob, node = heapq.heappop(h)
            curr_prob = -curr_prob

            if node in dist:
                continue
            
            dist[node] = curr_prob

            for neigh_node, neigh_prob in graph[node]:
                heapq.heappush(h, ((-1 * curr_prob * neigh_prob), neigh_node))
            
        if end_node in dist:
            return dist[end_node]
        
        return 0

        