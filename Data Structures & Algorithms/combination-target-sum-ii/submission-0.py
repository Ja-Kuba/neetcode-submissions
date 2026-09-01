class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []
        curr_sum  = 0
        nums = sorted(nums)
        
        def dfs(nums, subset, curr_sum, stind=0):
            if curr_sum > target:
                return
            elif curr_sum == target:
                res.append(subset.copy())
                return
            
            for i in range(stind, len(nums)):
                n = nums[i]
                if i > stind and n == nums[i-1]: 
                    continue
                if curr_sum+n > target:
                    break
                subset.append(n)
                dfs(nums, subset, curr_sum+n, i+1)
                subset.pop(-1)

        dfs(nums, subset, curr_sum)

        return res


"""
when go left we live all nums
if any right we remove current number - that ensures we do not have duplicates
"""


"""

nums = [2,5,6,9]
target = 9

"""