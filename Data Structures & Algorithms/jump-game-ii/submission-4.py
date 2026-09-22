class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_reach = 0
        jumps = 0
        next_jump = 0

        for i in range(0, len(nums)-1):
            curr_reach  = max(curr_reach, i+nums[i])
            if i == next_jump:
                jumps+=1
                next_jump=curr_reach
        
        return jumps
"""
ums = [2,4,1,1,1,1]
           ^     
        reach = 5
"""




