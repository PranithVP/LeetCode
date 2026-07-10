class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1

        direction = 'r'

        while left <= right and top <= bottom:
            if direction == 'r':
                for i in range(left, right+1):
                    res.append(matrix[top][i])
                top += 1
                direction = 'd'

            elif direction == 'd':
                for i in range(top, bottom+1):
                    res.append(matrix[i][right])
                right -= 1
                direction = 'l'

            elif direction == 'l':
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1
                direction = 'u'

            elif direction == 'u':
                for i in range(bottom, top-1, -1):
                    res.append(matrix[i][left])
                left += 1
                direction = 'r'

        return res