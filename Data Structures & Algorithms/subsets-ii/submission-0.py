class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []
        nums = sorted(nums)

        def dfs(nums,subset, sind = 0):
            res.append(subset.copy())
            for i in range(sind, len(nums)):
                if i > sind and nums[i] == nums[i-1]:
                    continue
                n = nums[i]
                subset.append(n)
                dfs(nums, subset, i+1)
                subset.pop()
                

        dfs(nums,subset)

        return res
