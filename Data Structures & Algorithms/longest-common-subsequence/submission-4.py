def printDp(dp, t1, t2):
    print("   -, " + ", ".join(list(t1)))
    t = "-" + t2
    for i, row in enumerate(dp):
        print(t[i], row)

class Solution:
    def longestCommonSubsequence(self, t1: str, t2: str) -> int:

        dp = [[0]*(len(t2)+1) for _ in range(len(t1)+1)]

        for i in range(0, len(t1)):
            for j in range(0, len(t2)):
                if t1[i] == t2[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[-1][-1]

