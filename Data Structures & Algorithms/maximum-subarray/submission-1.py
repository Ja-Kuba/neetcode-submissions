class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0]*(len(nums))
        dp[len(nums)-1] = nums[-1]

        """
        dp[i] max sum in at index i
        dp[i] = max(dp[i], dp[i]+dp[i+1])
        
        iterate from end 
        dp = nums.copy at the start

        """

        for i in range(len(nums)-2, -1, -1): 
            dp[i] = max(nums[i], nums[i]+dp[i+1])
        
        return max(dp)