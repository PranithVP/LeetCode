from typing import List

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    left, right = 0, len(matrix[0]) - 1
    top, bottom = 0, len(matrix) - 1
    found = False

    while top <= bottom:
        mid_row = (top + bottom) // 2
        if target >= matrix[mid_row][0] and target <= matrix[mid_row][-1]:
            found = True
            break
        elif target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            top = mid_row + 1

    if not found:
        return False
        
    while left <= right:
        mid_col = (left + right) // 2
        if matrix[mid_row][mid_col] == target:
            return True
        elif matrix[mid_row][mid_col] < target:
            left = mid_col + 1
        else:
            right = mid_col - 1
        
    return False
