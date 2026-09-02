class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWMAX= len(grid) -1 
        COLMAX= len(grid[0]) -1 
        time = 0
        fresh =  0 
        q = collections.deque()
        directions = [
            #row, col
            (-1, 0),
            ( 0,-1),
            ( 1, 0),
            ( 0, 1)
        ]

        for row, rows in enumerate(grid):
            for col, v in enumerate(rows):
                if v == 1:
                    fresh+=1
                elif v == 2:
                    q.append((row,col, 0)) 

        while q:
            r, c, t = q.popleft()
            time = max(t, time)
            for rd, cd in directions:
                nc = c + cd
                nr = r + rd
                if (0<=nc<=COLMAX and 0<=nr<=ROWMAX and 
                    grid[nr][nc] == 1
                ):
                    grid[nr][nc] = 2
                    fresh-=1
                    q.append((nr,nc, t+1))

        return time if fresh == 0 else -1




"""
basicly 
bfs cuz we want to check first each in the closest neighborhood 
then change them to rotten 

we should assume there may be more than one rotten?
 - then multi source bfs
 - otherwise clasic bfs is ok

Stop condition:
 1. if now fresh left
    we need to iterate first to check all rotten 
    count fresh

 2. cant get to the fresh
    if no new rotten - stop



"""