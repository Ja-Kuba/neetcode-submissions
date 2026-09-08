class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        # cache = [-1]*len(s)
        cache = {}

        def dfs(i) -> int:
            if i in cache:
                return cache[i]

            if i < len(s) and s[i] == '0':
                return 0
            if i+1 >= len(s):
                return 1 
                
            r = dfs(i+1)
            if 10<=int(s[i:i+2]) <= 26:
                r += dfs(i+2)
            cache[i] = r
            return r

        
        return dfs(0)





"""
we just care if  0 <= digit <= 26

[12342]
1 - 2 - 3 - cache()
12 
1 - 23  
      - 3 - 34 <-invalid

cache = {s_index: results}

stop conditions:
    invalid number: return 0
    end of s: return 1


dfs(i), dfs(i+1)



we can build dfs with cache



"""