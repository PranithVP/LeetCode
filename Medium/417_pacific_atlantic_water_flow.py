class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, visited):
            visited.add((r, c))

            for x, y in [(r-1, c), (r, c-1), (r+1, c), (r, c+1)]:
                if 0 <= x < m and 0 <= y < n:
                    if not (x, y) in visited and heights[x][y] >= heights[r][c]:
                        dfs(x, y, visited)

        for i in range(n):
            dfs(0, i, pacific)
            dfs(m-1, i, atlantic)

        for i in range(m):
            dfs(i, 0, pacific)
            dfs(i, n-1, atlantic)
        
        return list(pacific & atlantic)