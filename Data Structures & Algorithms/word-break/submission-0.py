class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False]*(len(s)+1)
        dp[len(s)] = True #<---position after last letter
        # if we reach to thath position we succesfully go
        # through all string

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s):
                    if w == s[i:i+len(w)]:
                      dp[i] = dp[i + len(w)]
                if dp[i]:
                    break


        return dp[0]  




        """
        n = len(s)
        dp[n] =  True - we are at the end of str
        dp[n-1]
         
        """