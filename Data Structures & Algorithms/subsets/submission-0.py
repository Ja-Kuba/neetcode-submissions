class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] 
        subset = []

        def dfs(nums,subset):
            res.append(subset.copy())
            for i, n in enumerate(nums):
                subset.append(n)
                dfs(nums[i+1:], subset)
                subset.pop()
                


        
        dfs(nums,subset)

        return res