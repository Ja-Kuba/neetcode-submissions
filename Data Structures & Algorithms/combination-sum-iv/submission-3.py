class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        # nums - [3,1,2]


        """

         3        1                   2     
        3 1 2   3 1      2          3  1 2  
                  3 1 2  3 1 2      ...        
               

        we can use bfs to early stop existing combos
        """

        cache = {}


        def dfs(v, t) ->int:
            if t in cache:
                return cache[t]

            if t == 0:
                return 1
            elif t < 0:
                return 0

            ret = 0
            for n in nums:
                ret+=dfs(n, t-n)
            
            cache[t] = ret
            return ret

        total = 0
        for n in nums:
            total+=dfs(n, target-n)

        return total