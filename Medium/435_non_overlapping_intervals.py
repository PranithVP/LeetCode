class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        
        if not intervals:
            return 0

        prev_end = intervals[0][1]

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i]
            if curr_start < prev_end:
                count += 1
                prev_end = min(prev_end, curr_end)
            else:
                prev_end = curr_end
        
        return count