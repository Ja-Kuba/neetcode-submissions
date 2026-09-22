class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[-1]
        gmax = nums[-1]
        for i in range(len(nums)-2, -1, -1): 
            curr = max(nums[i], nums[i]+curr)
            gmax = max(gmax, curr)

        return gmax


        """
        dp[i] max sum in at index i
        dp[i] = max(dp[i], dp[i]+dp[i+1])
        
        iterate from end 
        dp = nums.copy at the start

        """
