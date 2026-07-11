"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        h = []

        intervals.sort(key=lambda x: (x.start, x.end))

        for interval in intervals:
            start, end = interval.start, interval.end

            if h and h[0] <= start:
                heapq.heappop(h)
                heapq.heappush(h, end)
            else:
                heapq.heappush(h, end)

        return len(h)

