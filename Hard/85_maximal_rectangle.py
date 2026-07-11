class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        histograms = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                histograms[i][j] = int(matrix[i][j])

        for r in range(1, m):
            for c in range(n):
                if histograms[r][c] == 1:
                    histograms[r][c] = histograms[r-1][c] + 1
        
        max_area = 0

        for histogram in histograms:
            s = []

            for i in range(n):
                curr_start, curr_val = i, histogram[i]
                while s and s[-1][0] >= histogram[i]:
                    prev_val, prev_start = s.pop()
                    max_area = max(max_area, (i - prev_start) * prev_val)
                    curr_start = prev_start
                
                s.append((curr_val, curr_start))
            
            while s:
                val, start = s.pop()
                max_area = max(max_area, (n - start) * val)
        
        return max_area