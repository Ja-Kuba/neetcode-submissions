class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        

        cache:dict[int, int] = {}


        def dfs(i)->int:
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
            
            max_sum = max(
                nums[i],
                nums[i] + dfs(i+1)
            )

            cache[i] = max_sum
            return max_sum




        return max(dfs(i) for i in range(len(nums)))





'''
IN:
[int]: nums = [2,-3,4,-2,2,1,-1,4]
 nums -10,000 <= nums[i] <= 10,000


PROBLEM:
find the subarray -  is a contiguous non-empty sequence 
with the largest sum and return the sum


use dfs
cache = {index: maxsum}

dfs(i:int)

i:
MAX(
1. current
2. current + dfs(i+1)
)

if i >= len(nums):
    return 0






'''

