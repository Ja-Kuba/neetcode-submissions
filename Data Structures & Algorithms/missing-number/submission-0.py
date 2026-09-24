class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s=0
        nums_s = 0
        for i, n in enumerate(nums):
            nums_s+=n
            s+=i+1

        return s - nums_s






"""

[int]: nums len = n [0,n] no duplicates 


"""