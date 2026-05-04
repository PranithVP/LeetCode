class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(a, b):
            if a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]):
                return
            if grid[a][b] == 0:
                return
            
            grid[a][b] = 0
            self.curr += 1
            dfs(a+1, b)
            dfs(a-1, b)
            dfs(a, b+1)
            dfs(a, b-1)
        
        curr_max = 0
        self.curr = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    self.curr = 0
                    dfs(i, j)
                    curr_max = max(self.curr, curr_max)

        return curr_max