class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        ROWS, COLS = len(image), len(image[0])

        def dfs(x, y, old, new):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS:
                return
            
            if image[x][y] != old or image[x][y] == new:
                return
            
            image[x][y] = new
            
            dfs(x+1, y, old, new)
            dfs(x-1, y, old, new)
            dfs(x, y+1, old, new)
            dfs(x, y-1, old, new)

        dfs(sr, sc, image[sr][sc], color)
        return image
