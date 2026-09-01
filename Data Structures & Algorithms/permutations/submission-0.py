class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        seen = [False]*len(nums) # seen indexes falgs - allocate memmory first
        perm = []

        def dfs(seen, perm):
            last = True
            for i in range(len(nums)):
                if seen[i]:
                    continue
                last = False
                perm.append(nums[i])
                seen[i] = True
                dfs(seen, perm)
                seen[i] = False
                perm.pop()

            if last:
                res.append(perm.copy())


        dfs(seen, perm)
        
        
        return res