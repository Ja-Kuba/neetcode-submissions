def bs(l, r,intervals, target):
    # search for start position == target
    if l > r:
        return l

    m = (l+r) // 2
    v = intervals[m][0]
    if  v == target:
        return m
    elif target > v:
        return bs(m+1, r, intervals, target)
    else:
        return bs(l, m-1, intervals, target)


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        nst, nend = newInterval[0], newInterval[1]
        # we can use binnary search to find start and end index
        l = 0
        r = len(intervals) -1
        st_ind = bs(l, r, intervals, nst)
        end_ind = bs(l, r, intervals, nend)
        


        if st_ind > 0 and nst <= intervals[st_ind-1][1]:
            nst = intervals[st_ind-1][0]
            st_ind = st_ind-1

        if end_ind > 0 and nend <= intervals[end_ind-1][1]:
            nend = intervals[end_ind-1][1]
            print(f"{nend=}")

        if end_ind < len(intervals) and intervals[end_ind][0] == nend:
            nend = intervals[end_ind][1]
            end_ind += 1

        res = intervals[:st_ind] + [[nst, nend]] + intervals[end_ind:]
        

        return res




        # m = [4,9]  ints = [1,4] [4,5] [6,9] [9, 12]
        #                        ^1          ^3   
        # m = [3,9]  ints = [1,4] [4,5] [6,11] [11, 12]
        #                        ^1           ^3   
        # m = [4,11]  ints = [1,4] [4,5] [6,9] [9, 12]
        #                         ^1                   ^4




'''
intervals
intervals[i] = [start_i, end_i]

is initially sorted in ascending order by start_i.


newInterval = [start, end].

TASK:
insert newInterval
is still sorted in ascending order by start_i
still does not have any overlapping intervals
You may merge the overlapping intervals if needed

[1,2] and [2,3] are overlapping.

'''