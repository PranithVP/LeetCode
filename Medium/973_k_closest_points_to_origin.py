from typing import List
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        k_closest = []

        for x, y in points:
            heapq.heappush(k_closest, [-(x**2 + y**2), x, y])

            if len(k_closest) > k:
                heapq.heappop(k_closest)
        
        res = []
        while k_closest:
            _, a, b = heapq.heappop(k_closest)
            res.append([a, b])
        
        return res