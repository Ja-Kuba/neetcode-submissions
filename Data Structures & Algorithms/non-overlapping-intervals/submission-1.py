class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) < 2:
            return 0

        intervals.sort(key=lambda x: (x[0],x[1]))
        
        remove_cnt=0
        ci = 1
        li = 0
        while ci < len(intervals):
            c = intervals[ci]
            l = intervals[li]
            if (l[1] > c[0] ):
                #overlaping
                remove_cnt+=1
                #if abs(c[1] - c[0]) < abs(l[1] - l[0]):
                if  l[1] > c[1]:
                    li=ci
                ci+=1
            else:
                li=ci
                ci+=1


        return remove_cnt


# [[1, 2], [2, 4], [1, 4]] => remove [1,4] = return 1
# [[1, 6], [2, 3], [3, 4], [4, 5]] => remove [1,6] = return 1
# [[1, 2], [1, 6], [2, 100], [3, 4], [4, 5], [5,6], [6,7] ..., [99,100]]
# [[1, 6], [2, 4], [2, 100], [3, 4], [4, 5], [5,6], [6,7] ..., [99,100]]

'''
compare i-1 and i
if its overlaping take smaller: remove+=1
if its not take i as new 


'''

# [[1, 2], [2, 3], [3, 4], [4, 5], [1, 6]]


"""
[1, 2] and [2, 3] are non-overlapping.

[[int, int]]: intervals
    intervals[i] = [start_i, end_i]

we can have negative i:
    -50000 <= starti < endi <= 50000


return:
    the minimum number of intervals to remove
        to make the rest of the intervals non-overlapping



"""