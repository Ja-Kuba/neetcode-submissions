"""
1. State:
dp[i] = maximum product when breaking down integer i into at least 2 parts

len(dp) = n + 1

2. Choices:
For each number i, try breaking it at position j (where 1 ≤ j < i):
- Choice A: Keep the second part as is → j * (i - j)
- Choice B: Break the second part further → j * dp[i - j]

3. Recurrence:
dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
(Try all possible j values and keep the maximum)

4. Base case:
dp[1] = 1
(A single number 1 has product 1, though it can't actually be broken further)

5. Result:
dp[n]
(The maximum product achievable by optimally breaking down n)

"""


class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0]*(n+1)
        dp[1]=1 
        
        # [0, 1, 0, 0, 0]
        # [2,3,4] n = 4
        #  ^
        for i in range(2,n+1):
            best = 0
            for j in range(1, i):
                best = max(best, dp[i-j]*j, (i-j) *j)

            dp[i] = best


        return dp[n]













































