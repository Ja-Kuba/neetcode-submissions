class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {} #sum, path cnts 

        def dfs(s):
            if s in cache:
                return cache[s]

            if s>=n:
                ret = (n == s) 
            else:
                ret = dfs(s+1) + dfs(s+2)
            cache[s] = ret
            
            return ret  
        
        
        return dfs(0)
        