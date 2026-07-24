import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        q = [(queries[i], i) for i in range(len(queries))]
        q.sort()
        
        res = [0] * len(q)
        h = []
        i = 0
        
        for elem, idx in q:
            while i < len(intervals) and intervals[i][0] <= elem:
                heapq.heappush(h, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
                
            while h and h[0][1] < elem:
                heapq.heappop(h)
                
            if h:
                res[idx] = h[0][0]
            else:
                res[idx] = -1
         
        return res
            