class Solution:
    

    
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1   
    

        t = nums[0]
        min_val = nums[0]
        m = 0
        while l <= r:
            m = l + (r-l) //2 
            v = nums[m]
            print(v, l , r)
            if v < min_val:
                min_val = v

            if v >= t :
                # get the left side 
                l = m+1
            elif v < t:
                r = m-1
            else:
                break

        
        return min_val
            
            

            

            



"""
Input: nums = [3,4,5,6,1,2]
[f,f,f,f,t,t]


binnart serch
so we need to find the smallest number lower than nums[0]
target  < nums[0]

the index is shifts count

if t -> search left
if f -> search right




Output: 1

"""