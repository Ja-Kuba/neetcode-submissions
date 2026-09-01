class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]
        
        results = []
        state:list[int] = []
        
        tcols = set() #taken cols
        tup = set()   #taken diag up / r+c
        tdown = set()  #taken diag down \ r-c


        def dfs(row, state:list[int]):
            nonlocal results

            if row == n:
                #we have filled correctly all queens
                tmp = list()
                for q in state:
                    t = [("." if i!=q else "Q") for i in range(n)]
                    tmp.append("".join(t))
                results.append(tmp)
                    
                return

            for col in range(n):
                tup_val = row+col 
                tdown_val = row-col
                if col in tcols or tup_val in tup or tdown_val in tdown:
                    continue
                
                tcols.add(col)
                tup.add(tup_val)   # <--- best trick ever
                tdown.add(tdown_val) # <--- best trick ever
                state.append(col)
                dfs(row+1, state)
                state.pop()
                tcols.remove(col)
                tup.remove(tup_val)   
                tdown.remove(tdown_val) 
        
        dfs(0, state)
        return results

