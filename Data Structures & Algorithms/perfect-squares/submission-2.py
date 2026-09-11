"""
1. State:
dp[i] =  min steps to get to this sum 

len(dp) = n+1

2. Choices:
if sum == 0 return 
if sum < 0 break
if sum > 0 check next n step

3. Recurrence:
dp[i] = min(dp[i], 1+ dp[i-n])

4 Base case:
where to start dp

dp[0] = 0

5. Result:

dp[n]
"""



class Solution:
    def numSquares(self, n: int) -> int:
        sq = []
        if n == 1:
            return 1
        for i in range(1,n):
            s = i**2
            if s < n:
                sq.append(s)
            elif s == n:
                return 1

        dp = [n+10]*(n+1)
        dp[0] = 0
        # n=13 sq = [1,4,9]
        
        for i in range(1, n+1):
            for s in sq:
                if i-s >= 0:
                    dp[i] = min(dp[i], (dp[i-s]+1))
                
        
        return dp[n]















