class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = {} # index:cost
 
        def dfs(i) -> int:
            if i in cache:
                return cache[i]
            if i >= len(cost):
                return 0
            
            c=cost[i] + min(dfs(i+1), dfs(i+2))
            cache[i] = c

            return  c



        
        ret = min(dfs(0), dfs(1))

        return ret



        