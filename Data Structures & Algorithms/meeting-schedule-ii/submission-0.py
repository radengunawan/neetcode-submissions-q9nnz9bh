"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        time = []
        for i in intervals:
            time.append((i.start, 1))
            time.append((i.end, -1))

        time.sort(key=lambda x: (x[0], x[1]))

        res = count = 0
        for t in time:
            count += t[1]
            res = max(res, count)
        return res