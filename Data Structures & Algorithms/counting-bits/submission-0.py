class Solution:
    def countBits(self, n: int) -> List[int]:

        res=[]
        for i in range(0,n+1):
            res.append(0)
            v = i
            while v:
                v&=v-1
                res[i]+=1

        return res 



"""

 integer n
 in the range [0, n]
 
 number of 1ns

"""