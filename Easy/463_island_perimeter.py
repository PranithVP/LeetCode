class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        perimeter = 0
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n:
                return 1
            
            if grid[i][j] == 0:
                return 1
                
            if (i, j) in visited:
                return 0
                
            visited.add((i, j))
                
            return dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    perimeter += dfs(i, j)
        
        return perimeter