class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(a, b):
            if a < 0 or b < 0 or a >= len(grid) or b >= len(grid[0]):
                return
            if grid[a][b] == '0':
                return
            
            grid[a][b] = '0'
            dfs(a+1, b)
            dfs(a-1, b)
            dfs(a, b+1)
            dfs(a, b-1)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    print('test')
                    dfs(i, j)
                    count += 1
        return count