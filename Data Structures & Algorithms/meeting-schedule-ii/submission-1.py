"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # O(nlogn)
        inter = sorted(intervals, key=lambda x: x.start)

        max_overlaps = 0
        minh = []
        # O(n * (logn + logn) = nlogn) 
        for m in inter:
            while minh and minh[0] <= m.start:
                # O(logn)
                heapq.heappop(minh)

            # O(logn)
            heapq.heappush(minh,m.end)
            max_overlaps = max(max_overlaps, len(minh))
        
        # total O(nlogn + nlogn) = O(nlogn)
        return max_overlaps




"""
[Interval]: intervals
    [[start_1,end_1],[start_2,end_2],...]

minimum number of rooms required to schedule all meetings without any conflicts

BASICLY:
MAX(overlaping at onnce)

for empty its 1 or 0?

[0,3] [2,5] [4,6]
deque = [3,5]  
max =2 
[0,6] [2,5] [4,6]

"""