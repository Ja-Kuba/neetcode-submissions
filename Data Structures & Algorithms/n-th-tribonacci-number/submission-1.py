class Solution:
    cache = {}#{n : val}
    def tribonacci(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]

        if n in [1,2]:
            return 1
        elif n == 0:
            return 0
        ret = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.cache[n] = ret
        return ret
    






def fact(n:int) -> int:
    if n == 0:
        return 1 
    return n * fact(n-1)

def fact_it(n:int) -> int:
    fact = 1
    for i in range(1, n+1):
        fact*=i
    return fact


        
        

    
    """
    n0 = 0 
    n1 = 1
    n2 = 1 

    n3 = 1 + 1 + 0 = 2
    n4 = 2 + 1 + 1 = 4
    n5 = 4 + 2 + 1 = 7
    n6 = 5 + 4 + 2 = 11

    """







"""

Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

"""

Input: n = 3

Output: 2