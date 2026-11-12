"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        n = len(intervals)
        for i in range(n):
            A = intervals[i]
            for j in range(i + 1, n):
                B = intervals[j]
                if min(A.end, B.end) > max(A.start, B.start):
                    return False
        return True