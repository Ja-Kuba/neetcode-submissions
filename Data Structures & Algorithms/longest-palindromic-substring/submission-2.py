class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandCheck(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    l-=1
                    r+=1
            return l+1,r-1
        
        pL = 0 
        pR = 0
        for i in range(len(s)):
            lo,ro = expandCheck(i,i) #odd
            le,re = expandCheck(i,i+1) #even
            if ro - lo > pR-pL:
                pR,pL = ro, lo
            if re - le > pR-pL:
                pR,pL = re, le

        print(pL, pR)     

        return s[pL:pR+1]









# daaaaaaaaad
# if we start from the middle first palindrom we find is the longest
# possbilities prunning 
#   middle 1, -1, 2, -2, 3, -3
#   [dabababa]
#  start from i and i, i+1 

