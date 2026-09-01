class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []

        def dfs(nums,subset, sind = 0):
            res.append(subset.copy())
            for i in range(sind, len(nums)):
                n = nums[i]
                subset.append(n)
                dfs(nums[i+1:], subset)
                subset.pop()
                


        
        dfs(nums,subset)

        return res