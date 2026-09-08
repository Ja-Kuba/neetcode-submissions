class Solution:
    def countSubstrings(self, s: str) -> int:
        results=0

        def expandCheck(l,r):
            nonlocal results
            n = len(s)
            while l >= 0 and r < n and s[l] == s[r]:
                    results+=1
                    l-=1
                    r+=1
            
        
        for i in range(len(s)):
            expandCheck(i,i) #odd
            expandCheck(i,i+1) #even

        return results

