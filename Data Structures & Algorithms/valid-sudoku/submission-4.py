class Solution:
    def isValidSudoku2(self, board: List[List[str]]) -> bool:
        
        def add_to_set(s, ind, val) -> bool:
            if val in s[ind]:
                return False
            s[ind].add(val)
            return True

        def box_ind(col, row):
            a = math.floor(col/3)  
            b = math.floor(row/3) * 3
            # print(f"col: {col}, row: {row} => ({a}, {b}): {a+b}")

            return a + b        

        box_vals = [set() for _ in range(9)] 
        columns_vals = [set() for _ in range(9)]
        for i, row in enumerate(board):
            row_vals = set()
            for j, c in enumerate(row):
                # im checking if rows are ok
                if c == ".":
                    continue
                if c in row_vals: 
                    return False
                row_vals.add(c)
                
                #check box and columns
                if not (
                    add_to_set(box_vals,box_ind(i, j) ,c) and  
                    add_to_set(columns_vals,j,c)
                ):
                    return False

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                
                val = board[i][j]
                row_key = (val, i, "r")
                col_key = (val, j, "c")
                box_key = (i // 3, j // 3, val)
                
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        
        return True

"""
Input: board =
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]

Output: true
"""