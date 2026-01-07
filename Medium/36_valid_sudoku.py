from typing import List

def isValidSudoku(self, board: List[List[str]]) -> bool:
    #make a set for each row
    rows = [set() for _ in range(len(board))]

    #make a set for each column
    cols = [set() for _ in range (len(board[0]))]

    #make a set for each 3x3 segment
    segments = {}

    for a in range(3):
        for b in range(3):
            segments[(a, b)] = set()

    #add each element to each set, and while adding, if there is any overlap, return false
    for i in range(len(rows)):
        for j in range(len(cols)):
            if board[i][j] == '.':
                continue
            
            if board[i][j] in rows[i]:
                print(rows)
                return False
            rows[i].add(board[i][j])

            if board[i][j] in cols[j]:
                print(cols)
                return False
            cols[j].add(board[i][j])
            
            if board[i][j] in segments[(i//3, j//3)]:
                print(segments)
                return False
            segments[(i//3, j//3)].add(board[i][j])
                
    return True