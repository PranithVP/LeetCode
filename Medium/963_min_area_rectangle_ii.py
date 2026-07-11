from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        def dist(a, b):
            return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5

        n = len(points)
        diag_map = defaultdict(list)

        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                mx, my = x1+x2, y1+y2
                d = (y2-y1)**2 + (x2-x1)**2
                diag_map[(mx, my, d)].append([(x1, y1), (x2, y2)])

        min_area = float('inf')
        
        groups = diag_map.values()
        for group in groups:
            for i in range(len(group)):
                for j in range(i+1, len(group)):
                    p1, p2 = group[i]
                    p3, p4 = group[j]

                    if len(set([p1, p2, p3, p4])) != 4:
                        continue

                    min_area = min(min_area, dist(p1, p3) * dist(p1, p4))
        
        if min_area == float('inf'):
            return 0
        return min_area
                    