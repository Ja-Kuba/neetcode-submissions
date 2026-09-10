class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        longest = 1
        # nums = [9,1,4,2,9,3,7]
        # dp   = [1,1,1,2,1,2,1]

        for i in  range(n-1, -1, -1):
            curr = nums[i]
            for j in range(i+1, n):
                if nums[j] > curr and dp[j] >= dp[i]:
                    dp[i] = 1 + dp[j] 
                    longest = max(longest, dp[i])
                    
        

        return longest
