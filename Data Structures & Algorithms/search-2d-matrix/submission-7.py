class Solution:
    def get_mval(self, i, matrix) -> int:
        """
        get matrix value
        """
        x,y = 0,0

        m = len(matrix)
        n = len(matrix[0])

        #mp = (i - i%n)//n 
        mp = i // n
        np = i%n
        return matrix[mp][np]


    def binary_search(self, l:int, r:int, matrix: List[List[int]], target: int) -> bool:
        if l > r:
            return False 

        i = l + (r-l) // 2 
        v = self.get_mval(i, matrix)

        # ex.:
        # [0,1,2,3,4,5,6]  targret = 2
        #  l     i     r

        if v > target:
            # search left half
            return self.binary_search(l, i-1, matrix, target)
        elif v<target:
            return self.binary_search(i+1, r, matrix, target)
        else:
            return True
        


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if n == 0:
            return False
        l = 0
        r = m*n -1


        return self.binary_search(l, r, matrix, target)
        
    
    






"""
Input: matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10

Output: true
"""