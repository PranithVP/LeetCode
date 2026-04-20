from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        words = set()

        def dfs(k, i, j):
            if k == len(word):
                return True

            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == '#':
                return False
            
            if board[i][j] == word[k]:
                temp = board[i][j]
                board[i][j] = '#'
                res = (
                dfs(k+1, i + 1, j) or
                dfs(k+1, i - 1, j) or
                dfs(k+1, i, j + 1) or
                dfs(k+1, i, j - 1))
                board[i][j] = temp
                return res
            else:
                return False
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(0, i, j):
                    return True

        return False
            
