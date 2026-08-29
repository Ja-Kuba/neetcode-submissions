class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq_s1 = [0]*(ord('Z')-ord('A')+1)
        freq_wnd = [0]*(ord('Z')-ord('A')+1)

        for s in s1:
            #Both strings only contain lowercase letters.
            freq_s1[ord(s)-ord("a")]+=1

        l=0
        r=0

        while r < len(s1):
            s = s2[r]
            freq_wnd[ord(s)-ord("a")]+=1
            r+=1
        
        if freq_wnd == freq_s1:
            return True
        
        while r < len(s2):
            s = s2[r]
            ls=s2[l]
            freq_wnd[ord(s)-ord("a")]+=1
            freq_wnd[ord(ls)-ord("a")]-=1
            if freq_wnd == freq_s1:
                return True
            r+=1
            l+=1        

        return False




