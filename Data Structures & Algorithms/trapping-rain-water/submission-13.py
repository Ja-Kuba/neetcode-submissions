class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l,r = 0, len(height) - 1
        lmax=height[l]
        rmax=height[r]
        ret = 0
        #height=[0,1,0,2,1,0,1,3,2,1,2,1]
        while l < r:
            if lmax <= rmax:
                l+=1
                ret+=max(0, lmax-height[l]) 
                lmax = max(lmax, height[l])
                    

            else: # lmax > rmax:
                r-=1
                ret+=max(0,rmax - height[r])
                rmax = max(rmax, height[r])
                    

        return ret
