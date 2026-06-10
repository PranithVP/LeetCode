class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for a, b in intervals[1:]:
            recent_b = res[-1][1]
            if a > recent_b:
                res.append([a, b])
            else:
                res[-1][1] = max(recent_b, b)
        
        return res