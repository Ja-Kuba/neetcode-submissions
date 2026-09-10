class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        maxv = 0
        total = 0
        for n in nums:
            maxv = max(maxv,n)
            total+=n
        
        if total%2 != 0:
            return False

        half = total // 2 
        if maxv > half:
            return False
        

        dp = set()
        dp.add(0)
        for n in nums:
            newdp = dp.copy()
            for i in dp:
                if i + n == half:
                    return True
                elif i+n < half:
                    newdp.add(i+n)
            dp = newdp

        return False
                

                

            
            









"""

sum = 



"""



"""
Input: nums = [1,2,3,4]

Output: true

"""