class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s=len(nums)
        for i in range(len(nums)):
            s+=i

        return s - sum(nums)






"""

[int]: nums len = n [0,n] no duplicates 


"""