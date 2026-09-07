class Solution:
    def rob(self, nums):
        prev2 = 0  # dp[i-2]
        prev1 = 0  # dp[i-1]

        for x in nums:
            cur = max(prev1, prev2 + x)  # skip or rob current house
            prev2 = prev1
            prev1 = cur

        return prev1