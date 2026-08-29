class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l=0
        maxf=0
        for r, c in enumerate(s):
            #tracks characters in the window
            count[c] = 1+count.get(c, 0)
            maxf = max(maxf, count[c])

            if (r-l+1) - maxf > k:
                count[s[l]] -=1
                l+=1 

            res = max(res, r-l+1) # r-l+1 <-size of the window

        return res