class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        cache = {} # {(i,right): max_val}

        def dfs(left, right):
            if left > right:
                return 0
            if (left, right) in cache:
                return cache[(left, right)]
            
            max_val = nums[left] + max(
                dfs(left+2,right),
                dfs(left+3, right)
            )
            cache[(left,right)] = max_val
            return max_val

        # nums==[1,2,3]
        return max(
            dfs(0, len(nums)-2), dfs(1, len(nums)-2), 
            dfs(1, len(nums)-1), dfs(2, len(nums)-1)
        )




"""
[int]: nums 

nums[i] represents the amount of money the i
first house and the last house are neighbors
cant rob two adjacent houses
    [1,2,4] - only 4 can be robbed
    [1, 3, 5, 6 7]

Return:
    maximum amount of money you can rob without alerting the police.


dfs(left, right)

max dfs(0, len(nums)-2), dfs(1, len(nums)-1)

dfs[i] = we take i and i+2, or i+3

if i >= r:
    return 

[1,3,4,6]
 i   ^ ^

cache((i,right))

"""