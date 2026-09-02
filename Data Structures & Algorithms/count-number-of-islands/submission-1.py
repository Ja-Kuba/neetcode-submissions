class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0    
        directions =[
            (-1,  0),
            ( 0,  1),
            ( 0, -1),
            ( 1,  0)]
        rowsize = len(grid)-1
        colsize = len(grid[0])-1
        def printg(grid):
            print("__________")
            for row in grid:
                print("")
                for col, v in enumerate(row):
                    print(v, end="")
            print("")


        def bfs(row, col):
            q=collections.deque()
            q.append((row,col))
            
            while q:
                r, c = q.popleft() #get current field
                val = grid[r][c]
                if val == "0":
                    continue
                
                grid[r][c] = "0"
                for d in directions:
                    nc = min(max(0, c+d[0]), colsize)
                    nr = min(max(0, r+d[1]), rowsize)
                    q.append((nr, nc))





        for row, rows in enumerate(grid):
            for col, v in enumerate(rows):
                if v=="1":
                    bfs(row, col)
                    result+=1

        return result

        