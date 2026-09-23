class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sintervals = sorted(intervals, key=lambda x: x[0])
        
        res =[]
        cur_st = sintervals[0][0]
        cur_end = sintervals[0][1]
        for s in sintervals:
            sti, endi = s[0], s[1]
            if sti <= cur_end:
                cur_end = max(cur_end, endi)
            else:
                res.append([cur_st, cur_end])
                cur_st = sti
                cur_end = endi
        
        res.append([cur_st, cur_end])


        return res


# [1,6] [2, 9] [3, 8] [10,12]  => [1,9] [10, 12]





"""
[[int]]: intervals
intervals[i] = [start_i, end_i]

are intervals in any order?
"""