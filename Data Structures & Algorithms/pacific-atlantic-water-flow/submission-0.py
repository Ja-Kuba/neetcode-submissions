def printg(grid):
    print("__________")
    for row in grid:
        print("")
        for col, v in enumerate(row):
            print(v, end="")
    print("")


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [
            #row, col
            (-1, 0),
            ( 0,-1),
            ( 1, 0),
            ( 0, 1)]
        ranges = [] 
        results = []
        ROWSIZE = len(heights) -1 
        COLSIZE = len(heights[0]) -1
        PAC = 0
        ATL = 1

        


        def dfs(row, col, v, ocean):
            if ranges[row][col][ocean]:
                # node already visited by ocean
                return
            ranges[row][col][ocean] = True
            if ranges[row][col][ATL] and ranges[row][col][PAC]:
                # both can access add to results
                results.append([row,col])

            for rd, cd in directions:
                nr = row + rd 
                nc = col + cd
                if 0 <= nr <= ROWSIZE and 0 <= nc <= COLSIZE:
                    nv = heights[nr][nc]
                    if nv >= v:
                        dfs(nr,nc,nv,ocean)




        for i, rows in enumerate(heights):
            ranges.append(list())
            for r in rows:
                ranges[i].append([False, False])  # Pac, Atl

        for row, rows in enumerate(heights):
            for col, _ in enumerate(rows):
                if row == 0 or col == 0:
                    dfs(row,col,heights[row][col],PAC)
                if row == ROWSIZE or col == COLSIZE:
                    dfs(row,col,heights[row][col],ATL)



        printg(heights)
        printg(ranges)

        return list(results)
    
"""
ALG:

get range array matching size of grid

go from each ocen borders up and mark if u can get to the point (Pac:Bool, Atl: bool)
if dfs get to the point where Atl and Pac add to results
Early stops of DFS:
- node already has True

"""


