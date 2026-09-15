class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2) != len(s3):
            return False

        cache = {} #

        def dfs(i1, i2)->bool:
            if (i1, i2) in cache:
                return cache[(i1, i2)]
            if i1 == len(s1) and i2 == len(s2):
                return True
            
            i3 = i1+i2
            if i1 < len(s1) and s3[i3] == s1[i1]:
                if dfs(i1+1, i2):
                    cache[(i1, i2)] = True
                    return True


            if i2 < len(s2) and s3[i3] == s2[i2]:
                if dfs(i1, i2+1):
                    cache[(i1, i2)] = True
                    return True
            
            cache[(i1, i2)] = False
            return False
            


        return dfs(0,0)

'''

IN:
strings: s1, s2, and s3

OUT:
true if s3 == interleaving (s1 and s2) or false otherwise.


m,n - number of splits per s1, s2

keep track in which s1,s2 are we in
keep track of n,m splits count

if c not in s1 and s2: at ith position 
    False

iterate for c in s3:
        if c in s1 and not in s2:
           continue substring
        elif c in s2 and not in s1:
            split, curr_split = s2
        
        elif c in s2 and c in s1:
            split or continue        
        else: 
            return False



         
        


    if c in s2
        make a split
        or continue substring


'''