from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf') for _ in range(n)]
        prices[src] = 0
        
        for _ in range(k + 1):
            tmp = prices.copy()
            for u, v, p in flights:    
                if prices[u] == float('inf'):
                    continue

                if prices[u] + p < tmp[v]:
                    tmp[v] = prices[u] + p
                
            prices = tmp
            print(prices)
        
        if prices[dst] == float('inf'):
            return -1
        return prices[dst]