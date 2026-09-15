



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {} #{(i, tsum): result}
        
        def dfs(i, tsum):
            if (i, tsum) in cache:
                return cache[(i, tsum)]
            if i >= len(nums):
                return 1 if tsum == target else 0

            ret=dfs(i+1, tsum-nums[i])
            ret+=dfs(i+1, tsum+nums[i])

            cache[(i, tsum)] = ret
            return ret

        return dfs(0,0)





"""
IN:
[int]: array of integers nums 
int: tatget

for each i sum= +/-nums[i]
all nums are positve!

Two diff cases
0: "+1-1" and "-1+1".

each position is uniqe by index noy by value

target can be negative


2^n combinations to check

examples:
t=0

[9, 9, 18] 
[9, 9, 0]
[1000, 999, 1000, 999]

if sum neg or positve doesnt matter


dfs(i, tsum):
    if i >= len(nums):
        return 1 if tsum == target else 0
    
    ret=dfs(1, tsum-nums[i])
    ret+=dfs(1, tsum+nums[i])


"""























