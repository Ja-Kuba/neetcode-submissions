def pm(m):
    for r, row in enumerate(m):
        for c, v in enumerate(row):
            print(f"{v}, ", end="")
        print("")
    
    print("")

def zero_row(matrix, r):
    for i in range(0, len(matrix[0])):
        #change row
        matrix[r][i] = 0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        RM = len(matrix) - 1
        CM = len(matrix[0]) - 1 
        has_zero = False
        last_zero = False
        for r, row in enumerate(matrix):
            for c, v in enumerate(row):
                if v == 0:
                    has_zero = True
                    #change all left and top
                    for i in range(0, r):
                        #change top
                        if matrix[i][c] == 0:
                            break 
                        matrix[i][c] = 0    
                elif (r-1)>=0 and matrix[r-1][c] == 0:
                    matrix[r][c] = 0
      
            if last_zero:
                #after processing current row
                # zero last if needed
                zero_row(matrix,r-1)
            
            last_zero = has_zero
            has_zero = False
        
        if last_zero:
            zero_row(matrix,len(matrix)-1)


"""
we can go from left to right 
if 0 in row 


"""