class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums)-1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= reach:
                reach = i

        return True if reach == 0 else False




"""
INPUT
[int]: integer array nums
 nums[i] - maximum jump length at that position

RETURN:
true if you can reach the last index starting from index 0


dp[i]:bool - can reach end 

dp[i] = True if any dp[i+j] where j in range(nums[i])

dp[len(nums)] = True

return dp[0]

we only need to store smallest reachable index 

"""