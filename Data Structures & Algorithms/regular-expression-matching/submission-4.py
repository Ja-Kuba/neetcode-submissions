class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(ip, js) -> bool:
            if (ip, js) in cache:
                return cache[(ip, js)]

            if ip >= len(p):
                #if pattern is finished str also must be
                return js >= len(s)

            ret, r1, r2= False,False,False
            has_star = (ip+1 < len(p) and p[ip+1] == "*")
            
            match = (
                js<len(s)
                and (p[ip] == '.' or p[ip] == s[js])
            )

            if has_star:
                r1 = dfs(ip+2, js)
                if match:
                    r2 = dfs(ip, js+1)  
            elif match:
                ret = dfs(ip+1, js+1)


            cache[(ip, js)] = (ret or r1 or r2)            
            return (ret or r1 or r2)      

        return dfs(0,0)


'''
IN: 
str: s
 - lowercase english letters
str: p - regexp pattern 
    '.'  - Matches any single character
     '*' - Matches zero or more of the preceding element.


s = "aa", p = ".b"

aaabaabz .*bz



is, ip

is, ip = 0, 0
dfs(is,ip):
    curr_p = p[ip]
    if ip+1 > len(p) and p[ip+1] == "*" 
        curr_p = "c*"

    if curr_p[0] == '.' or curr_p[0] == s[is]:
        1. match and continue 
            dfs(is++,ip+len(curr_p))
        
        2. if curr_p[1] ==*
            dfs(is++, ip)

    else False  


    [c]<=>[.]

    [c*]




    if ip == len(p) and is == len(s):
        return True

state(ip,is)
cache(ip,is)

time, mem: O(n) = len(p)*len(s)


RETURN:
 bool: if match
'''

