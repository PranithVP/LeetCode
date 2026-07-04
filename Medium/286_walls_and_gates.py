from collections import deque

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:
        q = deque()
        m, n = len(grid), len(grid[0])
        visited = set()
        dist = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i, j))

        while q:
            queue_size = len(q)
            for _ in range(queue_size):
                r, c = q.popleft()

                if grid[r][c] == 2147483647:
                    grid[r][c] = dist

                for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    if 0 <= r + dr < m and 0 <= c + dc < n and (r+dr,c+dc) not in visited:
                        if grid[r+dr][c+dc] == 2147483647:
                            q.append((r+dr,c+dc))
                            visited.add((r+dr,c+dc))
        
            dist += 1




        