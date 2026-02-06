
def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s

    arr = [[""] * len(s) for _ in range(numRows)]
    dir = 'D'
    
    row, col = 0, 0
    for ch in s:
        arr[row][col] = ch
        if dir == 'D':
            row += 1
            if row == numRows - 1:
                dir = 'U'
        elif dir == 'U':
            row -= 1
            col += 1
            if row == 0:
                dir = 'D'
        
    return "".join([c for r in arr for c in r if c != ""])

print(convert("AB", 1))