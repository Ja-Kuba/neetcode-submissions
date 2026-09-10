class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        if max(nums) > target:
            return False

        # dp[s] = whether sum s is achievable
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            # traverse backward so each n is used at most once
            for s in range(target, n - 1, -1):
                if dp[s - n]:
                    dp[s] = True
            
            if dp[target]:
                return True

        return dp[target]
        