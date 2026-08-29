class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        l=0
        r=len(s1)
        ss = sorted(s1)

        while r <= len(s2):
            
            tmp = s2[l:r]
            if ss == sorted(tmp):
                return True
            l+=1
            r+=1
        
        return False




"""
Input: s1 = "abc", s2 = "lecabee"

Output: true
"""