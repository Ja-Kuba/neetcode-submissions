"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) < 2:
            return True


        intervals.sort(key=lambda x: x.start)
        
        last_end = 0

        for m in intervals:
            if m.start < last_end:
                return False
            last_end = m.end

        return True


'''

[]: meeting time interval
    [[start_1,end_1],[start_2,end_2],...] (start_i < end_i)
    
    unordered

TASK:
    could add all meetings without any conflicts.
    
    (0,8),(8,10) is ok
'''