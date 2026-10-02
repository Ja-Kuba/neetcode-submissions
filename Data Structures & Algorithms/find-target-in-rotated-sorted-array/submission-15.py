class Solution:
    def search(self, nums: List[int], target: int) -> int:
        


        def bsearch(l,r, t):
            if l>r:
                return -1
            m = (l+r)//2
            v = nums[m]
            if v == t:
                return m
            
            # check which half we are in
            if v >= nums[l]:
                # left sorterd part
                if t < nums[l]:
                    return bsearch(m+1, r, t)
                elif t > v:
                    return bsearch(m+1, r, t)
                else:
                    return bsearch(l, m-1, t)

            else:
                #right sorted part
                if t > nums[r]:
                    return bsearch(l, m-1, t)
                elif v > t:
                    return bsearch(l, m-1, t)
                else:
                    return bsearch(m+1, r, t)



        # [4,5,6,7,0,1,2]
        
        # nums = [3,4,5,6,1,2], target = 1
        #         l   m     r
        # nums = [5,1,3] t = 5
        #  



        
        return bsearch(0, len(nums)-1, target)