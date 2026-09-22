class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [2000] * len(nums)# 2000 cuz - 1 <= nums.length <= 1000
        dp[0] = 0
        
        for i in range(0, len(nums)-1):
            for j in range(nums[i]+1):
                if i+j < len(nums):
                    dp[i+j] = min(dp[i] + 1, dp[i+j])

        return dp[-1]

"""

[int]: nums
int: nums[i] represents the maximum length of a jump towards

j <= nums[i]
i + j < nums.length

start at 
    nums[0]

You may assume there is always a valid answer.

RETURN minimum number of jumps


dp[i] - minimal count of jumps to get at ith
dp[0] = 0

dp[i] = 1 + dp[last i] 

for i in range(0, len(nums))
    dp[i+j] = min(dp[i]+1, dp[i+j])



"""