class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s) < len(t):
            return 0

        cache = {} #(si, ti): int 

        def dfs(si:int, ti:int) -> int:
            if (si,ti) in cache:
                return cache[(si,ti)]
            # s = "cattt" t = "cat"
            if ti == len(t):
                return 1
            if si >= len(s):
                return 0
            res = 0
            if s[si] == t[ti]:
                res+=dfs(si+1, ti+1)
            
            res+=dfs(si+1, ti)

            cache[(si,ti)] = res
            return res


        return dfs(0,0)
        



'''

IN: 

str: two strings s and t

- english letters upper? lowwer?  casesensitivity??
- turn to lowwer as we do not know O(n) time O(1) space


ASK:
Return the number of distinct subsequences of s which are equal to t.

s always exists

start at each position of s
check for t


if s[i] == t[j]:
    1. continue s[i+1] t[j+1]
    2. skip s[i+1] t[j] to check if any other start
else:
    s[i+1]t[j] <=> same as 2

if j == len(t):
    return 1

we accumulate paths 
add cache for each i,j combination - O(len(t)len(s)) mem and time


'''