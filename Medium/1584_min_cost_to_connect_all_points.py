from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        total_cost = 0

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                a, b = points[i]
                a2, b2 = points[j]
                dist = abs(a2 - a) + abs(b2 - b)
                graph[(a, b)].append((dist, a2, b2))
                graph[(a2, b2)].append((dist, a, b))
        
        h = [(0, points[0][0], points[0][1])]


        while h:
            cost, x, y = heapq.heappop(h)
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            total_cost += cost

            if len(visited) == len(points):
                break

            for neigh in graph[(x, y)]:
                heapq.heappush(h, neigh)
        
        return total_cost


