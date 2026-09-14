class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {} # (r,c): paths cnt 
        

        def dfs(r,c):
            if (r,c) in cache:
                return cache[(r,c)]
            if r == m-1 and c == n-1:
                return 1

            cnt = 0
            if not r == m-1:
                cnt+=dfs(r+1, c)
            if not c == n-1:
                cnt+=dfs(r, c+1)
            
            cache[(r,c)] = cnt
            return cnt


        return dfs(0,0)

