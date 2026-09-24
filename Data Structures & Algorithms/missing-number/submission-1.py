class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)

        for i in range(len(nums)):
            m = m ^ i ^ nums[i] 
        
        return m