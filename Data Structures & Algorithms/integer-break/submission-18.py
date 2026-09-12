"""
definition:

dp[i] = max dot product for split of i
for i in range(1, n+1)
i - number to split


Conditions:
dp[i] = max(dp[i-j] * j, j*(i-j),dp[i])
for j in range(1, i) <= we cant get i = j as we want at lest 2 numbers

base:
d[1] = 1

result:
d[n]

"""

class Solution:
    def integerBreak(self, n: int) -> int:
        
        dp = [0]*(n+1)  
        dp[1] = 1

        for i in range(2,n+1):
            max_split = 0
            #s - first split int
            for s in range(1, i):
                # s*(i-s) do not split further check dot product of 2
                # dp[i-s]*s -> take s and try to split i-s
                max_split = max(max_split, dp[i-s]*s, s*(i-s))

            dp[i] = max_split

        return dp[n]
