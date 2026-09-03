def printg(grid):
    print("__________")
    for row in grid:
        print("")
        for col, v in enumerate(row):
            print(v, end="")
    print("")

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        directions = [
            #row, col
            (-1, 0),
            ( 0,-1),
            ( 1, 0),
            ( 0, 1)]
        ROWSIZE = len(board) -1 
        COLSIZE = len(board[0]) -1
        valid = set()

        def dfs(r,c):
            if (r,c) in valid or board[r][c] =='X':
                return
            valid.add((r,c))
            for rd, cd in directions:
                nr = r + rd
                nc = c + cd
                if 0 <= nr <= ROWSIZE and 0 <= nc <= COLSIZE:
                    dfs(nr,nc)

        for j in range(0, COLSIZE + 1):
            if board[0][j] == "O":
                dfs(0, j)
            if board[ROWSIZE][j] == "O":
                dfs(ROWSIZE, j)

        for i in range(1, ROWSIZE):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][COLSIZE] == "O":
                dfs(i, COLSIZE)
                

        for i in range(1,ROWSIZE):
            for j in range(1, COLSIZE):
                if board[i][j]=='O' and not (i,j) in valid: 
                    board[i][j]='X'
        