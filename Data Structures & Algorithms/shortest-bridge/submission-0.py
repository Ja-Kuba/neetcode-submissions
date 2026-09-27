class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        visited1 = set()
        visited0 = set()
        # we may also mark that in grid but im not sure we allowed as its binary
        N = len(grid)
        dirs = [(0,1), (1,0), (-1,0),(0,-1)]


        def find(r,c):
            q = collections.deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                if (r,c) in visited1:
                    continue
                if grid[r][c] == 0:
                    continue
                
                visited1.add((r,c))

                for rd, cd in dirs:
                    nr = r+rd
                    nc = c+cd
                    if 0 <= nr < N and 0<=nc < N: 
                        q.append((nr,nc))
        
        def shortest() -> int:
            q = collections.deque()

            for sr, sc in visited1:
                for rd, cd in dirs:
                    nr = sr+rd
                    nc = sc+cd
                    if 0 <= nr < N and 0<=nc < N: 
                        q.append((nr,nc, 0))
            
            while q: 
                r, c, d = q.popleft()
                if (r, c) in visited0 or (r, c) in visited1:
                    continue

                if grid[r][c] == 1:
                    return d

                visited0.add((r,c))
                for rd, cd in dirs:
                    nr = r+rd
                    nc = c+cd
                    if 0 <= nr < N and 0<=nc < N: 
                        q.append((nr,nc, d+1))

        for r, row in (enumerate(grid)):
            for c, v in enumerate(row):
                if v == 1:
                    find(r, c)
                    return shortest()




"""
nxn : grid - binary matrix
    1 - land
    0 - water

island - 4 directional, up,down, left, right?
there are 2 islands in the grid

minimum number of 0 to connect the islands

1. find 1st island
    - iterate matrix till firs 1
    - run bfs to find island

2. find shortest connection
    - run second bfs to find shortest connection

start from finding first island all 1s 
mark them as visited

then run bfs from each until find unvisited 1
we can also track visited zeros and prune them as this is bfs


- we can thinsk about not starting from middle island 1s but this is for later








"""