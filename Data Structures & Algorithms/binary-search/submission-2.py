class Solution:
    def binary_serach(self, l:int, r:int, nums:List[int], t:int) -> int:
        if l > r:
            # ex. [1] targe =2 
            return -1

        #m = (l + r) // 2  #  <-- for python is good to get just mean values
        m = l + (r - l) // 2 # for other languages r + l may overflow MAXINT
        # so we caluclate off to the middle of the l, r window and the shift 
        # it to l - pointer
        if nums[m] < t:
            return self.binary_serach(m+1, r, nums, t)
        elif nums[m] > t:
            return self.binary_serach(l, m-1, nums, t)
        else: # nums[m] == t:
            return m



    
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0  
        r = len(nums) -1             
 
        return self.binary_serach(l, r, nums, target)


    


"""
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3
"""