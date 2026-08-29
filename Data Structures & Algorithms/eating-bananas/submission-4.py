class Solution:
    """
    ineficient

    """

    def binary_search(self, 
        l:int,
        r:int,
        h:int, 
        piles:List[int]
    ) -> int:

        if l > r:
            return -1

        mk = l + (r-l) // 2
        
        need_h=0
        for p in piles:
            need_h+=math.ceil(p/mk)
        """
        k = [1,2,3,4,5,6,7,8] needed_k  = 5
                             
        """
        if need_h > h:
            # <=> k to small
            ret = self.binary_search(mk+1,r, h, piles)
            return ret
        else:# need_h <= h:
            # <==> check if k can be lower
            ret = self.binary_search(l,mk-1, h, piles)

            if ret > -1:
                return ret
            else:
                return mk





    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        return self.binary_search(l,r, h, piles)




        


"""


l = len(piles)



"""



"""
k = your bananas-per-hour eating rate of 


Input: piles = [1,4,3,2], h = 9
Output: 2
"""