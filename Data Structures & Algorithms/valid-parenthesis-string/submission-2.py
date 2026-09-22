class Solution:
    def checkValidString(self, s: str) -> bool:
        lMin = lMax = 0

        for c in s:
            
            if c == "(":
                lMin+=1
                lMax+=1

                
            elif c== ")":
                lMin-=1
                lMax-=1

            else: # c == '*'
                lMin-=1
                lMax+=1

            if lMax < 0:
                return False
            
            if lMin < 0:
                lMin = 0


        return lMin == 0
            