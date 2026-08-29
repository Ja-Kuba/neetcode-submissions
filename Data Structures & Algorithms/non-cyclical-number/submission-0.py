class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        ns = str(n)
        while not ns in seen:
            seen.add(ns)
            print(ns)
            sum = 0
            for d in ns:
                sum+=int(int(d)**2)
            if sum == 1:
                return True
            else:
                ns = str(sum)

        return False


"""
Input: n = 100

Output: true
"""