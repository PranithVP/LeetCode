import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        h = []
        visited = set()
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        heapq.heappush(h, (grid[0][0], 0, 0))
        
        while h:
            height, r, c = heapq.heappop(h)
            
            if r == n-1 and c == n-1:
                return height
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(h, (max(height, grid[nr][nc]), nr, nc))
            