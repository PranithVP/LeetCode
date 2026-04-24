from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        pos = set() # r - c
        neg = set() # r + c
        cols = set()
        board = [['.']*n for i in range(n)]

        def dfs(row):
            if row == n:
                res.append(["".join(a) for a in board])
                return
                    
            for c in range(n):
                if row + c not in neg and row - c not in pos and c not in cols:
                    board[row][c] = 'Q'
                    cols.add(c)
                    neg.add(row + c)
                    pos.add(row - c)
                    dfs(row+1)
                    board[row][c] = '.'
                    cols.remove(c)
                    neg.remove(row + c)
                    pos.remove(row - c)

        dfs(0)
        return res
