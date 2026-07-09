class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        point_set = set(tuple(p) for p in points)
        min_area = float('inf')

        for i in range(len(points)):
            for j in range(i+1, len(points)):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]

                    if x1 != x2 and y1 != y2:
                        if (x1, y2) in point_set and (x2, y1) in point_set:
                            min_area = min(min_area, abs((x2-x1) * (y2-y1)))
            
        if min_area == float('inf'):
            return 0
        
        return min_area