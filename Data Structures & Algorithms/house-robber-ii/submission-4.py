class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        def rob(i, stop):
            cache = {} # nums_ind: max_value

            def dfs(i) ->int:
                if i in cache:
                    return cache[i]
                if i > stop:
                    return 0

                r = nums[i] + max(dfs(i+2),dfs(i+3))
                cache[i] = r 

                return r

            return max(dfs(i), dfs(i+1))

        return max(rob(0, len(nums)-2), rob(1, len(nums)-1))