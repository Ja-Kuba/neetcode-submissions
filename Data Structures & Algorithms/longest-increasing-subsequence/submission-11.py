class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)

        for i in range(1, len(nums)):
            print(nums[i])
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        
        return max(dp)




'''
dp[0] = 1
dp[i] = 1 + max(dp[for j in 0:i]) where nums[j] < nums[i]

initial dp[i] = 1

solution max(dp)
'''
