class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = {}

        # i1 change to i2
        def dfs(i1, i2) -> int:
            if (i1,i2) in cache:
                return cache[(i1,i2)]

            if i1 >=len(word1):
                # w1 "cat"
                # w2 "cats"
                # add missing letters
                return len(word2) - i2              

            if i2 >=len(word2):
                # remove additional
                return len(word1) - i1
            
            operations = 0
            if word1[i1] == word2[i2]:
                operations += dfs(i1+1, i2+1)
            else:
                #remove
                remove = dfs(i1+1, i2)
                # insert
                insert = dfs(i1, i2+1)
                # replace
                replace = dfs(i1+1, i2+1)
                operations = 1 + min(remove, replace, insert)
            
            cache[(i1,i2)] = operations
            return operations
 
        return dfs(0,0)


'''


str: word1 and word2
    -  lowercase English letters.

3 operations on word1 unlimited number of times:
    1. Insert a character at any position
    2. Delete a character at any position
    3. Replace a character at any position

Return:
 the minimum number of operations to make word1  == word2.


word1="neatcdee", word2 = "neetcode"

"aaaadd" len=6    "aaabaa" len =7  

if w1 == w2:
    i1+1, i2+1
    
else:
    Insert
    remove
    delete

'''