class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = list()
        perm = []

        def dfs(perm):
            last = True
            for i in range(len(nums)):
                if nums[i] > 10:
                    continue
                last = False
                tmp = nums[i]
                perm.append(nums[i])
                nums[i] = 99
                dfs(perm)
                nums[i] = tmp
                perm.pop()


            if last:
                res.append(perm.copy())


        dfs(perm)
        
        
        return res