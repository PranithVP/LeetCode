"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: (x.start, x.end))

        reach = 0

        for interval in intervals:
            a, b = interval.start, interval.end
            if a < reach:
                return False
            reach = b
        
        return True
