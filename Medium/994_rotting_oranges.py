from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
        
        if not q:
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == 1:
                        return -1
            return 0
        
        count = -1
        while q:
            count += 1
            size = len(q)
            for _ in range(size):
                a, b = q.popleft()
                for x, y in [(a-1, b), (a, b-1), (a+1, b), (a, b+1)]:
                    if  0 <= x < len(grid) and 0 <= y < len(grid[0]):
                        if grid[x][y] == 1:
                            grid[x][y] = 2
                            q.append((x, y))
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return count