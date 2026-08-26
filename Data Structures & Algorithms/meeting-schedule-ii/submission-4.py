"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals)
        intervals.sort(key)
        """
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        d = {}
        for interval in intervals:
            d[interval.start] = d.get(interval.start, 0) + 1
            d[interval.end] = d.get(interval.end, 0) - 1
        
        ans = 0
        time_stamps = sorted(d.keys())
        open_intervals = 0
        for time in time_stamps:
            open_intervals += d[time]
            ans = max(ans, open_intervals)

        return ans

        

        