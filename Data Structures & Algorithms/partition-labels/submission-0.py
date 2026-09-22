class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occ = {}

        for i,c in enumerate(s):
            if c in occ:
                occ[c][1] = i
            else:
                occ[c] = [i,i]

        
        curr_st = 0
        curr_end = 0
        res = []
        for _, v in occ.items():
            st, end = v[0], v[1]
            if curr_end >= st:
                curr_end = max(curr_end, end)
            else:
                res.append(curr_end-curr_st+1)
                curr_st = st
                curr_end = end

        res.append(curr_end-curr_st+1)

        return res




'''

str: s
    lowercase english letters.

TASK:
split as many substrings as possible:
    each letter appears in at most one substring


"xyxxyzbzbbi"

x: 0, 3
y: 1, 4
z: 5, 7
b: 6, 9
i: 10, 10

dict = {
 letter: s  
}



'''