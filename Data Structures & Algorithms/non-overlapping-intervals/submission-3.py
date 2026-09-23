class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda x: (x[1],x[0]))
        l_end = -50000
        remove_cnt = 0
        for i in intervals:
            st, end = i[0], i[1]
            if l_end > st:
                #overlapping
                # we do not need to take min as intervals are sorted by end
                # l_end = min(l_end, end) 
                remove_cnt+=1
            else:
                l_end = end

        return remove_cnt


