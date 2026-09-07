class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {} # nums_ind: max_value

        if len(nums) < 3:
            return max(nums)

        def dfs(i) ->int:
            if i in cache:
                return cache[i]
            if i >= len(nums):
                return 0
             
            r = nums[i] + max(dfs(i+2),dfs(i+3))
            cache[i] = r 

            return r


        return max(dfs(0), dfs(1))
        

    
        # so [9, 1, 1, 9 ,7] <---
        #    [9, 1, 9, 8 , 7]
        #     ^  -  ^  ^
        #        ^     ^
        #    [9, 1, 1, 9, 9, 7]

