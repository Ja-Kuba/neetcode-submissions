class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_area = 0
        directions =[
            #row, col
            (-1,  0),
            ( 0,  1),
            ( 0, -1),
            ( 1,  0)]
        MAXROW = len(grid) - 1
        MAXCOL = len(grid[0]) -1 

        def dfs(row, col) -> int:
            if grid[row][col] == 0:
                return 0
            childs_area = 0
            grid[row][col] = 0  # <-- mark as visited
            for dr, dc in directions:
                nr = row+dr
                nc = col+dc
                if 0 <= nr <= MAXROW and 0 <= nc <= MAXCOL:
                    childs_area+=dfs(nr,nc)


            return 1 + childs_area


        for row, rvals in enumerate(grid):
            for col, val in enumerate(rvals):
                if val == 1:
                    area = dfs(row,col)
                    if area > max_area:
                        max_area = area
        
        return max_area