class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board) # rows
        n = len(board[0]) # cols

        if m <= 2 or n <= 2:
            return

        def dfs(x, y):
            if 0 > x or x >= m or 0 > y or y >= n or board[x][y] != 'O':
                return
            
            board[x][y] = 'T'
            dfs(x+1, y)
            dfs(x, y+1)
            dfs(x-1, y)
            dfs(x, y-1)


        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)
            if board[i][n-1] == 'O': dfs(i, n-1)
        for i in range(n):
            if board[0][i] == 'O': dfs(0, i)
            if board[m-1][i] == 'O': dfs(m-1, i)
        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'