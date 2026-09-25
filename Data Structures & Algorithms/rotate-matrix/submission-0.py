def mprint(m):
    for row in m:
        for v in row:
            print(f"{v}, ", end="")
        print("")
    
    print("")
    

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for d in range(len(matrix)):
            for s in range(1, len(matrix[0])-d):
                matrix[d+s][d], matrix[d][d+s] = matrix[d][d+s], matrix[d+s][d]



