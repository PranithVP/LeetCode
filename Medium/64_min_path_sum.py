class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = {}
        dp[(0, 0)] = grid[0][0]

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return float('inf')
            
            if (x, y) in dp:
                return dp[(x, y)]
            
            top = dfs(x-1, y) + grid[x][y]
            left = dfs(x, y-1) + grid[x][y]
            
            dp[(x, y)] = min(top, left)
            return dp[(x, y)]
            
        return dfs(m-1, n-1)