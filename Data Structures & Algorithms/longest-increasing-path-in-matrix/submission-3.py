class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        MAXR = len(matrix)
        MAXC = len(matrix[0])
        cache = {} #

        def dfs(r:int, c:int) -> int:
            if (r,c) in cache:
                return cache[(r,c)]
            curr_val = matrix[r][c]
            max_lip = 0
            for rd, cd in dirs:
                nr = r + rd
                nc = c + cd
                if (0 <= nr < MAXR and 0 <= nc < MAXC and 
                    matrix[nr][nc] > curr_val):
                    max_lip = max(max_lip, 1+dfs(nr,nc))

            cache[(r,c)] = max_lip
            return max_lip

        max_lip = 0
        for r in range(0, MAXR):
            for c in range(0, MAXC):
               max_lip = max(max_lip, 1+dfs(r,c))

        return max_lip
            




'''

IN:

[[int]]: 2-D grid of integers matrix
m[r][c] >= 0

Length longest strictly increasing path within matrix.
How we can move?:
- horiz, vertical
- NOT diagonally.

LIS - no DUPLICATES

so we can start at each position
but we can store longest incresing from this postion - cache(i,j):LIS from i,j



p [0][0]:
    - up
    - down
    - left
    - right
we do not need to track the visited as it wont match the constraints od LIS

RESULT: 
MAX(dfs)

Or maybe BFS?? - no benefits so stick with dfs
 

size of MATRIX? need to handle empty?

'''


