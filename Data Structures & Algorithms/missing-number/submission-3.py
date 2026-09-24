class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        s=len(nums)
        nums_s = 0
        for i, n in enumerate(nums):
            nums_s+=n
            s+=i

        return s - nums_s






"""

[int]: nums len = n [0,n] no duplicates 


"""