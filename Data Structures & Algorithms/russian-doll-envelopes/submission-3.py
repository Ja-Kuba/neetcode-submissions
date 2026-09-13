class Solution:
    def maxEnvelopes(self, envs: List[List[int]]) -> int:
        dp = [1]*len(envs)
        envs.sort(key=lambda x: (x[0], x[1]))
        for i in range(0, len(envs)):
            for j in range(0, len(envs)):
                if i == j: continue
                iw, ih = envs[i]
                jw, jh = envs[j]
                if iw > jw and ih > jh:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)



"""

dp[i] -> count of max enveloop stack with i as top

dp[] -> [1]*len(envelops)

choises:

dp[i] = max(dp wher both sizes smaller for j in 0, len(envelops))

time o(n) = n^2 
mem  O(n) = n




"""