"""
State:
i = curr target
dp[i] = count of combination
Choices:
1. if curr_targe > 0 -> dor n in nums: t-n
2. curr_target == 0 : return 1
3. curr_target < 0: return 0

Recurrence:
dp[i] = sum(dp[i-n] for each n)
# so its bottom => up
# i need smaller first

Base cases:
dp[0] = 1 as to get 0 return empty list

Answer:
dp[target]
"""

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        dp = [0]*(target+1)
        dp[0] = 1 # as 1 way to get zero - empty path

        t = target

        # dp [1, 0 ,0, 0 , 0] t= 4

        for t in range(0, target+1):
            for n in nums:
                if t-n >= 0:
                    dp[t] += dp[t-n]


        return dp[target]