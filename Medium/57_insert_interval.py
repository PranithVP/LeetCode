class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        res = []

        while i < len(intervals):
            start, end = intervals[i]
            newStart, newEnd = newInterval

            if end < newStart:
                res.append([start, end])
            elif start > newEnd:
                res.append(newInterval)
                return res + intervals[i:]
            else:
                newInterval = [min(start, newStart), max(end, newEnd)]

            i += 1
        
        res.append(newInterval)
        return res