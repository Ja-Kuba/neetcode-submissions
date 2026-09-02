class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [
            #row, col
            (-1, 0),
            ( 0,-1),
            ( 1, 0),
            ( 0, 1)
        ]
        INF = 2147483647
        ROWMAX= len(grid) -1 
        COLMAX= len(grid[0]) -1 
        # visit_count  = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        q = collections.deque()

        for row, rows in enumerate(grid):
            for col, val in enumerate(rows):
                if val == 0:
                    q.append((row,col))

    
        while q: 
            r, c = q.popleft()
            for rd, cd in directions:
                nc = c + cd
                nr = r + rd
                if 0<=nc<=COLMAX and 0<=nr<=ROWMAX and grid[nr][nc] == INF:
                    # IMPORTANT TO CHANGE FIRST CUZ OTHERWISE WE MIGHT 
                    # REVISIT IT WITH OLD VALUE FROM OTHER TREASURE
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc)) 