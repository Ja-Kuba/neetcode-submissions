class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        g = {c: set() for w in words for c in w}
        
        for j in range(0, len(words)-1):
            w1, w2 = words[j], words[j+1]
            for i in range(0,len(w1)):
                if i >= len(w2):
                    # w1: "hrf" w2: "hr"
                    return ""
                if w1[i] != w2[i]:
                    g[w1[i]].add(w2[i])
                    break

        visited = {}
        res = []

        def dfs(c):
            if c in visited:
                return visited[c]

            visited[c] = True
            for nc in g[c]:
                if dfs(nc): return "" # cycle detected
            
            visited[c] = False
            res.append(c)
            
            return False


        for c in g.keys():
            if dfs(c):
                #return True if cycle detected
                return ""  
        res.reverse()
        
        return "".join(res)




# [ab, abc] ok
# [abc, ab] return ""
 

'''
input
a-z  only lowwercas
we do not know order of alphabet
len(words) >= 1

words are sorted lexicographically 

input may be incorect -> return ""
- not in any lexicographically order

return:
- uniqe letters in order
- may be many solutions

'''
