class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        half = total // 2
        if max(nums) > half:
            return False


        dp = [False]*(half+1)
        dp[0] = True

        for n in nums: 
            for i in range(half, n-1, -1):
                if dp[i-n]:
                    dp[i] = True
            
                if dp[-1]:
                    return True

        return False
    