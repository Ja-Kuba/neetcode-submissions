"""
State:
i = curr target
dp[i] = number of ordered ways to make sum i
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

        # dp[t] = number of ordered ways to make sum t
        dp = [0] * (target + 1)

        # Base case:
        # There is exactly 1 way to make sum 0 -> choose nothing
        dp[0] = 1

        # Build answers from smaller targets to larger targets
        for t in range(1, target + 1):

            # Try every number as the LAST number used to form t
            for n in nums:

                # If n can fit as the last choice,
                # then all ways to make t-n can be extended by n
                if t - n >= 0:
                    dp[t] += dp[t - n]

        # Final answer: number of ways to make target
        return dp[target]