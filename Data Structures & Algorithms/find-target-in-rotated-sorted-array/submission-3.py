class Solution:
    

    def binary_search(self, l:int, r:int, nums:List[int], target:int) -> int:
        if l > r:
            return -1


        m = l + (r-l) //2
        print(nums[m])
        print(nums[l:r+1])
        t = target
        mv=nums[m]
        lv=nums[l]
        rv=nums[r]
        if t == mv :
            return m

        if lv <= mv:
            #left sorted portion
            if t > mv or t < lv:
                #right
                return self.binary_search(m+1, r, nums, target)
            elif t < mv and t >= lv:
                #left 
                return self.binary_search(l, m-1, nums, target)

        else:
            #right sorted portion
            if t < mv:
                #left
                return self.binary_search(l, m-1, nums, target)
            elif t > mv and t <= rv:
                #right
                return self.binary_search(m+1, r, nums, target)
            elif t > mv and t > rv:
                #left 
                return self.binary_search(l, m-1, nums, target)

        

    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l=0
        r=len(nums)-1
        ret = self.binary_search(l, r, nums, target)

        

        return ret



"""
Input: nums = [3,4,5,6,1,2], target = 1


Output: 4
"""