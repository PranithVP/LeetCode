class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[None] * len(matrix[0]) for _ in range(len(matrix))]
        max_path = 1
        
        def dfs(x, y):
            if dp[x][y]:
                return dp[x][y]
            
            res = 1

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if 0 <= x+dx < len(matrix) and 0 <= y+dy < len(matrix[0]):
                    if matrix[x+dx][y+dy] > matrix[x][y]:
                        res = max(res, dfs(x+dx, y+dy) + 1)
            
            dp[x][y] = res
            return res

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if not dp[i][j]: 
                    dfs(i, j)
                max_path = max(max_path, dp[i][j])
        
        return max_path