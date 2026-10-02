class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs= [(1,0), (0,1), (-1,0), (0,-1)]

        def search_bfs(row,col):
            
            q = collections.deque()
            q.append((row,col))
            maxrow = len(grid) -1 
            maxcol = len(grid[0]) - 1


            while q:
                r,c = q.popleft()
                if grid[r][c] == "0":
                    continue
                
                grid[r][c] = "0"

                for rd, cd in dirs:
                    nr = r + rd
                    nc = c + cd
                    if 0 <= nr <= maxrow and 0 <= nc <= maxcol:
                        q.append((nr,nc))
                    
        islands_cnt = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    islands_cnt+=1
                    search_bfs(row,col)

        return islands_cnt